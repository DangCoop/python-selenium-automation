from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class AccountSideMenu(Page):
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test = accountNav-signIn]")

    def sign_in_btn(self):
        self.click(*self.SIGN_IN_BTN)