from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')


@then('Verify there are {number} benefit cells')
def verify_benefit_cells(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[class*='cell-item-content']")
    assert len(cells) == number, f'Expected {number} cellss, but got {len(cells)}'
    print(cells)