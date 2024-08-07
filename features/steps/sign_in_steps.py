from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()
    # expected_text = 'Sign into your Target account'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0").text
    # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'


@when('Enter email "{email}" and password "{password}"')
def input_email_and_password(context, email, password):
    context.app.sign_in_page.input_email_and_password(email, password)


@when('Click Sign In With Password')
def click_sign_in_with_password(context):
    context.app.sign_in_page.sign_in_with_password()
    sleep(6)


@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_login()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()
    print(f'Original window => {context.original_window}')


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()
    sleep(3)


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def verify_pp_opened(context):
    context.app.terms_and_conditions_page.verify_tc_url()


@then('User can close new window')
def close(context):
    context.app.terms_and_conditions_page.close_page()

@then('User can switch back to original')
def return_to_original_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)

