from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import then, given, when
from time import sleep


@then('Verify search results shown for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_search_results(expected_product)
    # actual_text = context.driver.find_element(By.XPATH, "//div[@data-test = 'resultsHeading']").text
    # assert expected_product in actual_text, f'Expected {expected_product} is not in actual text {actual_text}'


@then('Verify correct search results URL opens for {expected_product}')
def verify_search_worked(context, expected_product):
    context.app.search_results_page.verify_product_in_url(expected_product)
    # url = context.driver.current_url
    # assert expected_product in url, f'Expected {expected_product} not in {url}'


@when('Select the first product from the search results')
def select_first_product(context):
    context.app.search_results_page.select_first_item()
    # #button = context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='addToCartButtonOrTextIdFor79545713']")))
    # button = context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button#addToCartButtonOrTextIdFor82572061")))
    # #context.driver.find_element(By.XPATH, "//*[@id='addToCartButtonOrTextIdFor79545713']").click()
    # button.click()
    # #sleep(20)


@when('Add the product to the cart')
def add_product_to_cart(context):
    context.app.cart_side_menu.add_product_to_cart()
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test= 'shippingButton']").click()


@then('Verify that the cue is in the cart')
def verify_cart(context):
    context.app.cart_side_menu.verify_cart()
    # expected_text = 'Added to cart'
    # actual_text = context.driver.find_element(By.XPATH, "//*[text()='Added to cart']").text
    # assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'


@then('Verify that search results has the product name and an image')
def verify_product_name(context):
    # To see ALL Listings (comment out if you only check the top ones):
    context.driver.execute_script("window.scrollBy(0, 4000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0, 4000)", "")

    all_product_items = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='product-title']" )

    for product in all_product_items:
        product_name = product.text
        assert product_name, "Product name is missing for an item"
        print(product_name)

        product_image = context.driver.find_element(By.CSS_SELECTOR, 'img')
        assert product_image.get_attribute('src'), f"Product image is missing for {product_name}."


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()


