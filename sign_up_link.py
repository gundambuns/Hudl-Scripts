# Login test - validate the 'sign up?' link sends the user to the sign up page
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
# Imports the chromedriver.exe file
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# set a wait time in case of a delayed connection
driver.implicitly_wait(1)

# opens chrome browser to hudl.com
driver.get("https://www.hudl.com")
# selects the log in button at the top right of the screen and clicks it
login_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/div/a[2]').click()
# on the log in screen, user selects the 'sign up' link
sign_up = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[2]/a').click()
# on the login help page, verify that the url is the help page url
get_url = driver.current_url
print("register" in get_url)
# close browser
time.sleep(1)
driver.quit()