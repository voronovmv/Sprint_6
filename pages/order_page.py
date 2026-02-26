import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import order_page_locators as loc
from pages.order_2nd_step_page import OrderPage2ndStep


class OrderPage(BasePage):

    @allure.step("Открыть оформление заказа через верхнюю кнопку")
    def open_order_top(self):
        self.accept_cookies_if_present()
        self.click_safe(loc.ORDER_TOP_BUTTON)

    @allure.step("Открыть оформление заказа через нижнюю кнопку")
    def open_order_bottom(self):
        self.accept_cookies_if_present()
        self.click_safe(loc.ORDER_BOTTOM_BUTTON)

    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro(self, metro: str):
        metro_input = self.wait_for_visibility(loc.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(Keys.CONTROL, "a")
        metro_input.send_keys(Keys.BACKSPACE)
        metro_input.send_keys(metro)

        option_locator = loc.metro_option(metro)
        self.wait_for_presence(option_locator)
        self.click_safe(option_locator)

        # иногда список не закрывается — добиваем клавиатурой
        try:
            self.wait.until(EC.invisibility_of_element_located(option_locator))
        except Exception:
            metro_input.send_keys(Keys.ARROW_DOWN)
            metro_input.send_keys(Keys.ENTER)

    @allure.step("Заполнить первый шаг заказа")
    def fill_personal_data(self, name: str, surname: str, address: str, metro: str, phone: str) -> OrderPage2ndStep:
        self.accept_cookies_if_present()

        self.type_text(loc.NAME, name)
        self.type_text(loc.SURNAME, surname)
        self.type_text(loc.ADDRESS, address)
        self.select_metro(metro)
        self.type_text(loc.PHONE, phone)

        self.click_safe(loc.NEXT_BUTTON)

        # важно: следующий Page Object создаём внутри Page Object, а не в тесте
        return OrderPage2ndStep(self.driver)
