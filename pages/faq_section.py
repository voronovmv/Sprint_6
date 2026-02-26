import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import faq_section_locators as loc


class FaqSection(BasePage):

    @allure.step("Открыть вопрос FAQ с индексом {index}")
    def open_question(self, index: int):
        self.scroll_to(loc.FAQ_TITLE)
        self.click_safe(loc.question(index))
        self.wait.until(EC.visibility_of_element_located(loc.answer(index)))
        self.wait_text_not_empty(loc.answer(index))

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_answer_text(self, index: int) -> str:
        self.scroll_to(loc.answer(index))
        return self.wait_text_not_empty(loc.answer(index))
