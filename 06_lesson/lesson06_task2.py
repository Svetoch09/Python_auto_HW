from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))

driver.get("http://uitestingplayground.com/textinput")
# --- Actions ---
# 1. Define locators/input
input_text_locator = "#newButtonName"  # CSS Selector for the input field
button_locator = "#updatingButton"     # CSS Selector for the button

# 2. Type text into the input field
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

# 3. Click the button to update its name
click_button = driver.find_element(By.ID, "updatingButton")
click_button.click()

# --- Wait and Verification ---
wait = WebDriverWait(driver, 10, 0.5)
wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, button_locator), "SkyPro")
)
print(driver.find_element(By.ID, "updatingButton").text)
driver.quit()
