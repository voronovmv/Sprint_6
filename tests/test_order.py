import allure
import pytest

from pages.main_page import MainPage
from pages.order_page_2nd_step import OrderPage2ndStep
from utils.data_generator import generate_person_data, generate_rent_data


@allure.feature("Order")
@allure.story("Оформление заказа")
@pytest.mark.parametrize("entry_point, seed", [("top", 1), ("bottom", 2)])
def test_order_flow(driver, entry_point, seed):
    allure.dynamic.title(f"Заказ самоката: вход={entry_point}")

    person = generate_person_data(seed)
    rent = generate_rent_data(seed)

    page = MainPage(driver)
    order = page.order()

    if entry_point == "top":
        order.open_order_top()
    else:
        order.open_order_bottom()

    order.fill_personal_data(**person)

    second_step = OrderPage2ndStep(driver)
    second_step.fill_rent_data(**rent)
    second_step.confirm_order()
    second_step.check_order_success()