import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class FaqSection(BasePage):
    FAQ_TITLE = (By.XPATH, "//div[contains(@class,'Home_SubHeader') and contains(.,'Вопросы о важном')]")

    def question(self, index: int):
        return (By.ID, f"accordion__heading-{index}")

    def answer(self, index: int):
        return (By.ID, f"accordion__panel-{index}")

    @allure.step("Открыть вопрос FAQ с индексом {index}")
    def open_question(self, index: int):
        self.scroll_to(self.FAQ_TITLE)
        self.click_safe(self.question(index))
        self.wait.until(EC.visibility_of_element_located(self.answer(index)))
        self.wait_text_not_empty(self.answer(index))

    @allure.step("Получить текст ответа FAQ с индексом {index}")
    def get_answer_text(self, index: int) -> str:
        self.scroll_to(self.answer(index))
        return self.wait_text_not_empty(self.answer(index))