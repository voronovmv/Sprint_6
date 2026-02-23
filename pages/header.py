import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Header(BasePage):
    SCOOTER_LOGO = (By.XPATH, "//a[@href='/' and .//img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']/parent::a")

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_safe(self.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_safe(self.YANDEX_LOGO)