import allure

from pages.main_page import MainPage
from utils.constants import BASE_URL, DZEN_PART


@allure.feature("Navigation")
@allure.story("Логотип Самокат")
def test_scooter_logo_opens_main(driver):
    allure.dynamic.title("Лого Самокат ведет на главную")

    page = MainPage(driver)
    header = page.header()

    header.click_scooter_logo()
    assert header.current_url() == BASE_URL


@allure.feature("Navigation")
@allure.story("Логотип Яндекс")
def test_yandex_logo_opens_dzen_in_new_window(driver):
    allure.dynamic.title("Лого Яндекс открывает Дзен в новой вкладке")

    page = MainPage(driver)
    header = page.header()

    url = header.open_dzen_and_get_url(DZEN_PART)
    assert DZEN_PART in url