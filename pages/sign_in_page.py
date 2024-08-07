from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep

class SignInPage(Page):
    SIGN_IN_PAGE_MSG = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0")
    EMAIL_INPUT_FIELD = (By.ID, 'username')
    PASS_INPUT_FIELD = (By.ID, 'password')
    SIGN_IN_WITH_PASS = (By.CSS_SELECTOR, "#login")
    SIGN_IN_FORM = (By.CSS_SELECTOR, ".sc-fe064f5c-0")
    TC_LINK =(By.XPATH, "//a[text()='Target terms and conditions']")


    def click_tc_link(self):
        self.click(*self.TC_LINK)

    def verify_sign_in_form(self):
        expected_text = 'Sign into your Target account'
        actual_text = self.driver.find_element(*self.SIGN_IN_PAGE_MSG).text
        assert expected_text == actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

    def input_email_and_password(self, email, password):
        self.input_text(email, *self.EMAIL_INPUT_FIELD)#.send_keys(email)
        self.input_text(password,*self.PASS_INPUT_FIELD)#.send_keys(password)

    def sign_in_with_password(self):
        self.click(*self.SIGN_IN_WITH_PASS)

    def verify_user_login(self):
        self.wait_for_element_disappear(*self.SIGN_IN_FORM)