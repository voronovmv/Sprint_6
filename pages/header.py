import allure

from pages.base_page import BasePage
from locators import header_locators as loc


class Header(BasePage):

    @allure.step("Нажать на логотип Самоката")
    def click_scooter_logo(self):
        self.click_safe(loc.SCOOTER_LOGO)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_safe(loc.YANDEX_LOGO)

    @allure.step("Открыть Дзен по клику на логотип Яндекса и вернуть URL")
    def open_dzen_and_get_url(self, dzen_part: str) -> str:
        self.click_yandex_logo()
        self.wait_for_windows(2)
        self.switch_to_window(1)
        self.wait_url_not_blank()
        self.wait_url_contains(dzen_part)
        return self.current_url()
