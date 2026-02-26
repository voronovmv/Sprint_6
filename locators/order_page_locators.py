from selenium.webdriver.common.by import By

ORDER_TOP_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[normalize-space(text())='Заказать']")
ORDER_BOTTOM_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[normalize-space(text())='Заказать']")

NAME = (By.XPATH, "//input[@placeholder='* Имя']")
SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
PHONE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")

NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")

def metro_option(metro: str):
    return (
        By.XPATH,
        "//div[contains(@class,'select-search__select')]//button[contains(@class,'select-search__option') and normalize-space(.)="
        f"'{metro}']"
    )
