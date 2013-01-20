from selenium import webdriver
# For keyboard keys
from selenium.webdriver.common.keys import Keys

# Setup
driver = webdriver.Firefox()
driver.get("http://www.pandora.com")

# Find and login
elem = driver.find_element_by_name("sign in")

# Finding elements
elem = driver.find_element_by_name("Password")
elem.send_keys("tryingout")
elem.send_keys(Keys.RETURN)

driver.close()
