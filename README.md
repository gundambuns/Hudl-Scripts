Hudl test-scripts

Included are 8 python scripts interacting and testing the initial login page for hudl.com. The intention is to display my automation test skills, as someone who has worked in positions which only required manual testing up to this point.

All of the testing utilizes the chrome webdriver, which would need to be downloaded to the following filepath: C:\Program Files (x86)\chromedriver.exe (filepath will need to be adjusted if downloaded to a different location or if macOS/linux is used as the OS to run the script.

The scripts provided cover accessing the hudl.com site, accessing the login page, and then going through various different flows to validate that the login functionality is working as intended.
Scripts can be run via the command prompt/powershell or via programs such as Visual Studio Code or another IDE.

Notes: 
> Most of the scripts contain the variables 'user_email' and 'user_password'. These variables are near the top of the respective scripts and are currently set to '0', and would need to have a valid email and password entered in place of '0' to successfully run the script
> driver.implicitly_wait is set to 1, but can be adjusted if a longer amount of time is needed
> time.sleep is set to 3 at the end of each script, but isn't necessary. time.sleep is in place to allow the last screen that has been arrived on to be viewed, in case of debugging and visual confirmation of the script

