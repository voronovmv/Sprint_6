import allure
import pytest

from pages.main_page import MainPage
from utils.data_generator import generate_person_data, generate_rent_data


@allure.feature("Order")
@allure.story("Оформление заказа")
@pytest.mark.parametrize("open_method, seed", [("open_order_top", 1), ("open_order_bottom", 2)])
def test_order_flow(driver, open_method, seed):
    allure.dynamic.title(f"Заказ самоката: вход={open_method}")

    person = generate_person_data(seed)
    rent = generate_rent_data(seed)

    page = MainPage(driver)
    order = page.order()

    # без if/else
    getattr(order, open_method)()

    second_step = order.fill_personal_data(**person)
    second_step.fill_rent_data(**rent)
    second_step.confirm_order()

    assert second_step.is_order_success_visible()
