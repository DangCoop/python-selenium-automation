from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    EMPTY_CART_MSG = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0")
    def verify_empty_cart_msg(self, expected_text):
        expected_text = 'Your cart is empty'
        actual_text = self.driver.find_element(*self.EMPTY_CART_MSG).text
        assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'