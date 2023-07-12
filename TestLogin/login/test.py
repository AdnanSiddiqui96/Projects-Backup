from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# create an instance of webdriver and specify the browser you want to use
driver = webdriver.Chrome()

# navigate to the login page
driver.get("https://ukcrm.dev-hi.xyz/login")

# enter the username and password and click the login button
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")
email.send_keys("adnan@hnhtechsolutions.com")
password.send_keys("12345678")
login_button = driver.find_element(By.ID, "submit-login")
login_button.click()
time.sleep(5)