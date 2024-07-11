from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.XPATH, "//button[@data-test ='@web/Search/SearchButton']").click()
    sleep(6)

@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()
    sleep(3)

@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.sc-58ad44c0-3").click()
    sleep(7)

@then('From right side navigation menu, click Sign In')
def navigation_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test = accountNav-signIn]").click()


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify header has {number} link')
def verify_header_link_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
    print(links)