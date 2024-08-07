from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test ='@web/Search/SearchButton']")
CART_ICON_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open()
    #context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    #context.driver.find_element(*SEARCH_BTN).click()
    #sleep(6) # Can't Replaced this sleep method by ether implicitly or explicitly method! if it possible please help!


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.cart_btn()
    # button = context.driver.wait.until(EC.element_to_be_clickable(CART_ICON_BTN))
    # #context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']").click()\
    # button.click()
    # #sleep(3)

@when('Click Sign In')
def click_sign_in(context):
    context.app.header.sing_in_btn()
    #context.driver.find_element(By.CSS_SELECTOR, "span.sc-58ad44c0-3").click()
    #sleep(7) Replaced by context.driver.implicitly_wait(4)

@when('From right side navigation menu, click Sign In')
def navigation_menu(context):
    context.app.account_side_menu.sign_in_btn()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test = accountNav-signIn]").click()


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='utilityHeaderContainer']")


@then('Verify header has {number} link')
def verify_header_link_amount(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
    print(links)
    # Make a loop to click all 6 links
    for i in range(len(links)):
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        links[i].click()
        sleep(4)