import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[normalize-space(text())='Заказать']")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[normalize-space(text())='Заказать']")

    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")

    METRO_OPTION = (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]//button[contains(@class,'select-search__option') and normalize-space(.)='{metro}']"
    )

    NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")

    def _type(self, locator, text: str):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.click()
        el.send_keys(Keys.CONTROL, "a")
        el.send_keys(Keys.BACKSPACE)
        el.send_keys(text)
        return el

    @allure.step("Открыть оформление заказа через верхнюю кнопку")
    def open_order_top(self):
        self.accept_cookies_if_present()
        self.click_safe(self.ORDER_TOP_BUTTON)

    @allure.step("Открыть оформление заказа через нижнюю кнопку")
    def open_order_bottom(self):
        self.accept_cookies_if_present()
        self.click_safe(self.ORDER_BOTTOM_BUTTON)

    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro(self, metro: str):
        metro_input = self.wait.until(EC.visibility_of_element_located(self.METRO_INPUT))
        metro_input.click()
        metro_input.send_keys(Keys.CONTROL, "a")
        metro_input.send_keys(Keys.BACKSPACE)
        metro_input.send_keys(metro)

        option_locator = (self.METRO_OPTION[0], self.METRO_OPTION[1].format(metro=metro))
        self.wait.until(EC.presence_of_element_located(option_locator))
        self.click_safe(option_locator)

        try:
            self.wait.until(EC.invisibility_of_element_located(option_locator))
        except Exception:
            metro_input.send_keys(Keys.ARROW_DOWN)
            metro_input.send_keys(Keys.ENTER)

    @allure.step("Заполнить первый шаг заказа")
    def fill_personal_data(self, name: str, surname: str, address: str, metro: str, phone: str):
        self.accept_cookies_if_present()

        self._type(self.NAME, name)
        self._type(self.SURNAME, surname)
        self._type(self.ADDRESS, address)
        self.select_metro(metro)
        self._type(self.PHONE, phone)

        self.click_safe(self.NEXT_BUTTON)