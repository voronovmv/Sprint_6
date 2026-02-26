import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from pages.base_page import BasePage
from utils.constants import BASE_URL


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(BASE_URL)

    BasePage(driver).accept_cookies_if_present()

    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            allure.attach(
                driver.current_url,
                name="url",
                attachment_type=allure.attachment_type.TEXT,
            )