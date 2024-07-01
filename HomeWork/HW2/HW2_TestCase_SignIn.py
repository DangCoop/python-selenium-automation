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
driver.get('https://www.target.com/')
# Click SignIn button
driver.find_element(By.XPATH, "//span [@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
#  Click SignIn from side navigation
driver.find_element(By.XPATH, "//a [@data-test= 'accountNav-signIn']").click()
sleep(10)

sing_in_text = driver.find_element(By.XPATH, "//h1//span[text()='Sign into your Target account']")

sing_in_button = driver.find_element(By.XPATH, "//button[@type= 'submit']")

if sing_in_text and sing_in_button:
    print("Sign In page opened successfully.")
else:
    print("Sign In page did not open.")

#sleep(6)