from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager()
                                                  .install()))

driver.get("http://the-internet.herokuapp.com/login")
user_name_locator = "[name='username']"
password_locator = "[name='password']"
login_button_locator = "[type='submit']"

username_field = driver.find_element(By.CSS_SELECTOR, user_name_locator)
username = username_field.send_keys("tomsmith")
password_field = driver.find_element(By.CSS_SELECTOR, password_locator)
password = password_field.send_keys("SuperSecretPassword!")
login_button = (driver.find_element(By.CSS_SELECTOR, login_button_locator)
                .click())

green_text_locator = "#flash"
green_text = driver.find_element(By.CSS_SELECTOR, green_text_locator).text
print(green_text)
driver.quit()
