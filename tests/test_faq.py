import pytest
import allure

from pages.main_page import MainPage
from utils.test_data import FAQ_DATA


@allure.feature("FAQ")
@allure.story("Вопросы о важном")
@pytest.mark.parametrize("index, question, expected_answer", FAQ_DATA)
def test_faq_answer_text_matches_question(driver, index, question, expected_answer):
    allure.dynamic.title(f"FAQ: {question}")

    page = MainPage(driver)
    faq = page.faq()

    faq.open_question(index)
    actual = faq.get_answer_text(index).strip()

    assert actual == expected_answer