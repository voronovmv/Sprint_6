import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class OrderPage2ndStep(BasePage):
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR_DAY = (
        By.XPATH,
        "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'react-datepicker__day--outside-month')) and normalize-space(text())='{day}']"
    )

    RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")
    RENT_PERIOD_OPTION = (By.XPATH, "//div[contains(@class,'Dropdown-option') and normalize-space(text())='{text}']")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space(text())='Заказать']")

    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]")
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space(text())='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]//div[contains(text(),'Заказ оформлен')]")

    @allure.step("Открыть календарь")
    def open_calendar(self):
        self.click_safe(self.DATE_INPUT)

    @allure.step("Выбрать дату доставки: {day}")
    def select_delivery_day(self, day: int):
        self.open_calendar()
        day_locator = (self.CALENDAR_DAY[0], self.CALENDAR_DAY[1].format(day=day))
        self.wait.until(EC.visibility_of_element_located(day_locator))
        self.click_safe(day_locator)

    @allure.step("Выбрать срок аренды: {period_text}")
    def select_rent_period(self, period_text: str):
        self.click_safe(self.RENT_PERIOD_DROPDOWN)
        option_locator = (self.RENT_PERIOD_OPTION[0], self.RENT_PERIOD_OPTION[1].format(text=period_text))
        self.wait.until(EC.visibility_of_element_located(option_locator))
        self.click_safe(option_locator)

    @allure.step("Выбрать цвет самоката: {color}")
    def select_color(self, color: str):
        if color == "black":
            self.click_safe(self.COLOR_BLACK)
        elif color == "grey":
            self.click_safe(self.COLOR_GREY)

    @allure.step("Заполнить комментарий: {comment}")
    def fill_comment(self, comment: str):
        self.type_text(self.COMMENT_INPUT, comment)

    @allure.step("Заполнить второй шаг заказа: дата='{date_day}', срок='{period}', цвет='{color}', комментарий='{comment}'")
    def fill_rent_data(self, date_day: int, period: str, color: str, comment: str):
        self.select_delivery_day(date_day)
        self.select_rent_period(period)
        self.select_color(color)
        self.fill_comment(comment)

    @allure.step("Нажать кнопку Заказать на втором шаге")
    def click_order_button(self):
        self.click_safe(self.ORDER_BUTTON)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_order_button()
        self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MODAL))
        self.click_safe(self.CONFIRM_YES_BUTTON)

    @allure.step("Проверить, что заказ успешно оформлен")
    def check_order_success(self):
        self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MODAL))