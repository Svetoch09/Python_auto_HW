from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
           "loading-images.html")
waiter = WebDriverWait(driver, 10, 0.5)

text_locator = "#text"
picture_locator = "#award"
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, text_locator),
                                     "Done!"))

pic_attribute = (driver.find_element(By.CSS_SELECTOR, picture_locator)
                 .get_attribute("src"))
print(pic_attribute)
driver.quit()
