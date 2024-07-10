from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search worked')
def verify_search_worked(context):
    expected_text = 'tea'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
