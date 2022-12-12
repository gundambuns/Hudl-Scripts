# Hudl Icon Test - user selects the login button, taking the user to the login page; user is able to interact with the Hudl icon to take the user back to hudl.com
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
# on the log in screen, user selects clicks on the Hudl icon in the center of the screen and is redirected to hudl.com
hudl_icon = driver.find_element(By.XPATH, '/html/body/div[1]/section/div[2]/div/form/a').click()
# user is redirected back to the hudl.com site
get_url = driver.current_url
print("hudl.com" is get_url)
# close browser
time.sleep(1)
driver.quit()