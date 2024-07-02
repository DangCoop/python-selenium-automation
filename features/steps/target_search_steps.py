from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
@when('Search for product')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')

    context.driver.find_element(By.XPATH, "//button[@data-test ='@web/Search/SearchButton']").click()
    sleep(6)
@then('Verify search worked')
def verify_search_worked(context):
    expected_text = ('tea')
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


#Verifies that “Your cart is empty” message is shown on the cart icon
@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(3)

@then('Verify “Your cart is empty” message is shown')
def veryfi_empty_cart_text(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

#Verify that a logged out user can navigate to Sign In

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.sc-58ad44c0-3").click()
    sleep(7)

@then('From right side navigation menu, click Sign In')
def navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = accountNav-signIn]").click()

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    expected_text = 'Sign into your Target account'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.styles__StyledHeading-sc-1awz1yh-0").text
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'