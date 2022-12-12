# Login test - user selects the log in button on hudl.com, enters in their username and password, selects the remember user checkbox, and then selects the  log in button
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
#check remember me button
remember_me_button = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[2]/div/form/div/div[4]/div/label').click()
user_login_button = driver.find_element(By.ID, 'logIn').click()
html1 = driver.current_url
#close browser
#open browser again and going to hudl.com, verifying that url link will redirect to hudl.com/home, logged into the correct user
driver = webdriver.Chrome(PATH)
driver.get("https://www.hudl.com")
html2 = driver.current_url
#compare html 1 to html 2 and verify they match
html1 is html2
#delay in time to verify that the home page displays
time.sleep(1)
driver.quit()