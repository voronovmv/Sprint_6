from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)

from locators import base_page_locators as loc


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout, poll_frequency=0.2)

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

    def click_safe(self, locator):
        self.scroll_to(locator)

        def _try_click(driver):
            try:
                el = driver.find_element(*locator)
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
                try:
                    el.click()
                except ElementClickInterceptedException:
                    driver.execute_script("arguments[0].click();", el)
                return True
            except (ElementClickInterceptedException, StaleElementReferenceException):
                return False

        self.wait.until(lambda d: _try_click(d))

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

    def switch_to_window(self, index: int):
        self.driver.switch_to.window(self.driver.window_handles[index])

    def wait_url_not_blank(self):
        def _predicate(driver):
            return driver.current_url and driver.current_url != "about:blank"

        return self.wait.until(_predicate)

    def wait_url_contains(self, part: str):
        return self.wait.until(EC.url_contains(part))

    def current_url(self) -> str:
        return self.driver.current_url

    def accept_cookies_if_present(self):
        try:
            banner = WebDriverWait(self.driver, 2, poll_frequency=0.2).until(
                EC.presence_of_element_located(loc.COOKIE_BANNER)
            )
            if banner.is_displayed():
                self.driver.find_element(*loc.COOKIE_BUTTON).click()
        except TimeoutException:
            return