from selenium import webdriver
# For keyboard keys
from selenium.webdriver.common.keys import Keys

# Headless display
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()

# Setup
driver = webdriver.Firefox()
driver.get("http://www.pandora.com")

# Find and login
signinLink = driver.find_element_by_xpath('//a[@class="signInLink underline"]')
signinLink.click()


# Finding elements
# elem = driver.find_element_by_name("Password")
# elem.send_keys("tryingout")
# elem.send_keys(Keys.RETURN)

driver.close()
display.stop()
