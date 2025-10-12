from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager()
                                                .install()))
driver.get("http://uitestingplayground.com/dynamicid")
stable_css_locator = ".btn-primary"
blue_button = driver.find_element(By.CSS_SELECTOR, stable_css_locator)
dynamic_id = blue_button.get_attribute('id')
# get attribute id for this button
print(f"Dynamic id for this button: {dynamic_id}")
# print attribute to console
blue_button.click()
driver.quit()
