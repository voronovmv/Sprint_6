import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage


@allure.feature("Navigation")
@allure.story("Логотип Самокат")
def test_scooter_logo_opens_main(driver):
    allure.dynamic.title("Лого Самокат ведет на главную")

    page = MainPage(driver)
    header = page.header()

    header.click_scooter_logo()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


@allure.feature("Navigation")
@allure.story("Логотип Яндекс")
def test_yandex_logo_opens_dzen_in_new_window(driver):
    allure.dynamic.title("Лого Яндекс открывает Дзен в новой вкладке")

    page = MainPage(driver)
    header = page.header()

    header.click_yandex_logo()

    page.wait_for_windows(2)
    driver.switch_to.window(driver.window_handles[1])

    page.wait_url_not_blank()
    WebDriverWait(driver, 10).until(EC.url_contains("dzen"))

    assert "dzen" in driver.current_url