from selenium.webdriver.common.by import By
from behave import given, when, then

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} is not in actual text {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_search_worked(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'
