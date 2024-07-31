from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class Header(Page):
    SEARCH_FIELD = (By.ID, "search")
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SING_IN_BTB = (By.CSS_SELECTOR, "span.sc-58ad44c0-3")

    def search_product(self, search_item):
        self.input_text(search_item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        # wait for the page with search results to load
        sleep(6)

    def cart_btn(self):
         self.click(*self.CART_BTN)
         sleep(8)

    def sing_in_btn(self):
        self.click(*self.SING_IN_BTB)