from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import then, given, when
from time import sleep

@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    assert expected_product in actual_text, f'Expected {expected_product} is not in actual text {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_search_worked(context, expected_product):
    url = context.driver.current_url
    assert expected_product in url, f'Expected {expected_product} not in {url}'


@when('Select the first product from the search results')
def select_product(context):
    #button = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='addToCartButtonOrTextIdFor79545713']")))
    button = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#addToCartButtonOrTextIdFor82572061")))
    #context.driver.find_element(By.XPATH, "//*[@id='addToCartButtonOrTextIdFor79545713']").click()
    button.click()
    #sleep(20)


@when('Add the product to the cart')
def add_product_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test= 'shippingButton']").click()

@then('Verify that the cue is in the cart')
def verify_cart(context):
    expected_text = 'Added to cart'
    actual_text = context.driver.find_element(By.XPATH, "//*[text()='Added to cart']").text
    assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
