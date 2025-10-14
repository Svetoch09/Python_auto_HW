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

last_picture_locator = "#image-container img:nth-of-type(4)"
picture_locator = "#image-container img:nth-child(3)"
all_pictures = waiter.until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, last_picture_locator))
)

pic_attribute = (driver.find_element(By.CSS_SELECTOR, picture_locator)
                 .get_attribute("src"))
print(pic_attribute)
driver.quit()
