from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(12)

# Amazon LOGO
driver.find_element(By.XPATH,"//i[@class= 'a-icon a-icon-logo']")

# "Create Account" Header
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# "Your Name" field
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

# "Email" field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

# Password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# Password characters info
driver.find_element(By.CSS_SELECTOR, ".a-box.a-alert-inline.a-alert-inline-info")

# "Re-enter Password" field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

# "Create Your Account" Button
driver.find_element(By.CSS_SELECTOR, "#continue")

# "Conditions of Use" link
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

# "Privacy Notice" link
driver.find_element(By.CSS_SELECTOR, "[href='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# "Sign In" link
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")