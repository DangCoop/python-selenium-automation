from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()
    # expected_text = 'Sign into your Target account'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

@when('Enter email "{email}" and password "{password}"')
def input_email_and_password(context, email, password):
    context.app.sign_in_page.input_email_and_password(email, password)

@when('Click Sign In With Password')
def click_sign_in_with_password(context):
    context.app.sign_in_page.sign_in_with_password()
    sleep(6)

@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_login()
