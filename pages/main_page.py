from pages.base_page import BasePage
from pages.header import Header
from pages.faq_section import FaqSection
from pages.order_page import OrderPage


class MainPage(BasePage):
    def header(self) -> Header:
        return Header(self.driver)

    def faq(self) -> FaqSection:
        return FaqSection(self.driver)

    def order(self) -> OrderPage:
        return OrderPage(self.driver)