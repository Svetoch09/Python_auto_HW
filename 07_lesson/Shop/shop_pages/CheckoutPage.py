from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class CheckoutPage:
    FIRST_NAME_LOCATOR = (By.ID, "first-name")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    ZIP_CODE_LOCATOR = (By.ID, "postal-code")
    CONTINUE_BTN_LOCATOR = (By.ID, "continue")
    TOTAL_SUM_LOCATOR = (By.XPATH, "//div[@data-test='total-label']")

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10)

    def fill_info(self, first_name, last_name, zip_code):
        first_name_field = self.waiter.until(EC.visibility_of_element_located
                                             (self.FIRST_NAME_LOCATOR))
        first_name_field.send_keys(first_name)
        last_name_field = self.waiter.until(EC.visibility_of_element_located
                                            (self.LAST_NAME_LOCATOR))
        last_name_field.send_keys(last_name)
        zip_code_field = self.waiter.until(EC.visibility_of_element_located
                                           (self.ZIP_CODE_LOCATOR))
        zip_code_field.send_keys(zip_code)

    def continue_checkout(self):
        continue_btn = self.waiter.until(EC.element_to_be_clickable
                                         (self.CONTINUE_BTN_LOCATOR))
        continue_btn.click()

    def get_total_sum(self):
        total_sum_element = self.waiter.until(EC.visibility_of_element_located
                                              (self.TOTAL_SUM_LOCATOR))
        return total_sum_element.text

    def check_sum(self, expected_sum, actual_total_text):
        assert expected_sum in actual_total_text, (
            f"Ошибка! Ожидаемая сумма: '{expected_sum}',"
            f"но получено: '{actual_total_text}'")
