from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartSideMenu(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test= 'shippingButton']")
    ADD_TO_CART_MSG = (By.XPATH, "//*[text()='Added to cart']")

    def add_product_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_cart(self):
        self.verify_text('Added to cart', *self.ADD_TO_CART_MSG)