from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignInPage(Page):
    SIGN_IN_PAGE_MSG = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0")

    def verify_sign_in_form(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE_MSG).text
        assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
