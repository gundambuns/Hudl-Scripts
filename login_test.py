# Login test - user selects the log in button on hudl.com, enters in their username and password, and then selects the  log in button on the log in page
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
# Imports the chromedriver.exe file
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#set a wait time in case of a delayed connection
driver.implicitly_wait(1)
# input in the userid and password used for this test
user_email = "0"
user_password = "0"

#opens chrome browser to hudl.com
driver.get("https://www.hudl.com")
#selects the log in button at the top right of the screen and clicks it
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/a[2]').click()
#on the user/password screen, enter in the email address and the password
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(user_email)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(user_password)
user_login_button = driver.find_element(By.ID, 'logIn').click()
html1 = driver.current_url
#close browser
time.sleep(3)
driver.quit()