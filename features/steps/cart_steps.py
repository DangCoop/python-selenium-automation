from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify “Your cart is empty” message is shown')
def veryfi_empty_cart_text(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'




