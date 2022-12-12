# Login test - user attempts to login via an organization account, request should send the user back to the original login screen
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
# Imports the chromedriver.exe file
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# set a wait time in case of a delayed connection
driver.implicitly_wait(1)
# input in the userid and password used for this test
user_email = "0"
user_password = "0"

# opens chrome browser to hudl.com
driver.get("https://www.hudl.com")
# selects the log in button at the top right of the screen and clicks it
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/a[2]').click()
# on the log in screen, user selects the 'log in with an organization button'
organization_button = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[2]/div/form/div/a/button').click()
# on the organization login page, the user email is entered into the email field
email_field = driver.find_element(By.ID, "uniId_1")
email_field.send_keys(user_email)
# log in button is clicked
user_login_button = driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div/form/div[1]/button').click()
#user is returned to the initial login page, validate that the login does not work via the organization page via getting the url and verifying it has 'login' in the url
get_url = driver.current_url
print("login" in get_url)
# close browser
time.sleep(1)
driver.quit()