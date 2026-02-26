from selenium.webdriver.common.by import By

FAQ_TITLE = (By.XPATH, "//div[contains(@class,'Home_SubHeader') and contains(.,'Вопросы о важном')]")

def question(index: int):
    return (By.ID, f"accordion__heading-{index}")

def answer(index: int):
    return (By.ID, f"accordion__panel-{index}")
