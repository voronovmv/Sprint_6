import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import order_2nd_step_page_locators as loc


class OrderPage2ndStep(BasePage):

    @allure.step("Открыть календарь")
    def open_calendar(self):
        self.click_safe(loc.DATE_INPUT)

    @allure.step("Выбрать дату доставки: {day}")
    def select_delivery_day(self, day: int):
        self.open_calendar()
        day_locator = loc.calendar_day(day)
        self.wait.until(EC.visibility_of_element_located(day_locator))
        self.click_safe(day_locator)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rent_period(self, period_text: str):
        self.click_safe(loc.RENT_PERIOD_DROPDOWN)
        option_locator = loc.rent_period_option(period_text)
        self.wait.until(EC.visibility_of_element_located(option_locator))
        self.click_safe(option_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color: str):
        color_map = {
            "black": loc.COLOR_BLACK,
            "grey": loc.COLOR_GREY,
        }
        self.click_safe(color_map[color])

    @allure.step("Заполнить комментарий: {comment}")
    def fill_comment(self, comment: str):
        self.type_text(loc.COMMENT_INPUT, comment)

    @allure.step("Заполнить второй шаг заказа")
    def fill_rent_data(self, date_day: int, period: str, color: str, comment: str):
        self.select_delivery_day(date_day)
        self.select_rent_period(period)
        self.select_color(color)
        self.fill_comment(comment)

    @allure.step("Нажать кнопку Заказать на втором шаге")
    def click_order_button(self):
        self.click_safe(loc.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_order_button()
        self.wait.until(EC.visibility_of_element_located(loc.CONFIRM_MODAL))
        self.click_safe(loc.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен (bool)")
    def is_order_success_visible(self) -> bool:
        el = self.wait.until(EC.visibility_of_element_located(loc.SUCCESS_MODAL))
        return el.is_displayed()
