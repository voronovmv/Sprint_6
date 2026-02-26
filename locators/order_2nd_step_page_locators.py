from selenium.webdriver.common.by import By

DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

RENT_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class,'Dropdown-control')]")

COLOR_BLACK = (By.ID, "black")
COLOR_GREY = (By.ID, "grey")

COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[normalize-space(text())='Заказать']")

CONFIRM_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]")
CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Modal')]//button[normalize-space(text())='Да']")
SUCCESS_MODAL = (By.XPATH, "//div[contains(@class,'Order_Modal')]//div[contains(text(),'Заказ оформлен')]")

def calendar_day(day: int):
    return (
        By.XPATH,
        "//div[contains(@class,'react-datepicker__day') and not(contains(@class,'react-datepicker__day--outside-month')) "
        f"and normalize-space(text())='{day}']"
    )

def rent_period_option(text: str):
    return (By.XPATH, f"//div[contains(@class,'Dropdown-option') and normalize-space(text())='{text}']")
