import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException


class BasePage:
    COOKIE_BANNER = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator):
        el = self.wait_for_presence(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    def click_safe(self, locator, retries: int = 3):
        last_exc = None
        for _ in range(retries):
            try:
                el = self.scroll_to(locator)
                self.wait_for_clickable(locator).click()
                return
            except (ElementClickInterceptedException, StaleElementReferenceException) as exc:
                last_exc = exc
                time.sleep(0.2)
            except Exception as exc:
                last_exc = exc
                try:
                    el = self.scroll_to(locator)
                    self.driver.execute_script("arguments[0].click();", el)
                    return
                except Exception:
                    time.sleep(0.2)
        raise last_exc

    def type_text(self, locator, text: str, clear: bool = True):
        el = self.wait_for_visibility(locator)
        self.scroll_to(locator)
        el.click()
        if clear:
            el.send_keys(Keys.CONTROL, "a")
            el.send_keys(Keys.BACKSPACE)
        el.send_keys(text)
        return el

    def wait_text_not_empty(self, locator):
        def _predicate(driver):
            text = driver.find_element(*locator).text.strip()
            return text if text else False

        return self.wait.until(_predicate)

    def wait_for_windows(self, count: int):
        return self.wait.until(EC.number_of_windows_to_be(count))

    def wait_url_not_blank(self):
        def _predicate(driver):
            return driver.current_url and driver.current_url != "about:blank"

        return self.wait.until(_predicate)

    def accept_cookies_if_present(self):
        try:
            banner = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(self.COOKIE_BANNER))
            if banner.is_displayed():
                self.driver.find_element(*self.COOKIE_BUTTON).click()
        except TimeoutException:
            return