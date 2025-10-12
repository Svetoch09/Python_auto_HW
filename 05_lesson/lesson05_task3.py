from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))

driver.get("http://the-internet.herokuapp.com/inputs")
field_input_locator = "input[type]"
field_input = driver.find_element(By.CSS_SELECTOR, field_input_locator)
sky = field_input.send_keys("Sky")      # input "Sky"
clear_field = field_input.clear()       # clear the field
pro = field_input.send_keys("Pro")      # input "Pro"
driver.quit()
