from selenium.webdriver.common.by import By
from behave import then, given, when


@given('Open Help page for Returns')
def click_cart(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option}')
def select_topic(context, option):
    context.app.help_page.select_topic(option)


@then('Verify help {expected_text} page opened')
def verify_help_page_header(context, expected_text):
    context.app.help_page.verify_header(expected_text)


# @then('Verify help {expected_text} page opened')
# def verify_help_page_header_promotions(context, expected_text):
#     context.app.help_page.verify_promotions()

