from selenium import webdriver
# For keyboard keys
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

# Headless display
# from pyvirtualdisplay import Display
# display = Display(visible=0, size=(800, 600))
# display.start()

# Setup
driver = webdriver.Firefox()
driver.get("http://www.pandora.com")
wait = ui.WebDriverWait(driver, 10)

# Find and login
signinLink = driver.find_element_by_xpath("//a[@class='signInLink underline']")
wait.until(lambda driver: driver.find_element_by_xpath("//a[@class='signInLink underline']").is_displayed())
#wait.until(lambda x: siginInLink.isDisplayed())
signinLink.click()


# Finding elements
# elem = driver.find_element_by_name("Password")
# elem.send_keys("tryingout")
# elem.send_keys(Keys.RETURN)

driver.close()
#display.stop()
