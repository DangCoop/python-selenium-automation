from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()
    # expected_text = 'Sign into your Target account'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'