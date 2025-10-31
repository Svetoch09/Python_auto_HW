from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BTN_LOCATOR = (By.XPATH, "//button[@id='checkout']")

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10)

    def checkout(self):
        check_out = self.waiter.until(EC.element_to_be_clickable
                                      (self.CHECKOUT_BTN_LOCATOR))
        check_out.click()
