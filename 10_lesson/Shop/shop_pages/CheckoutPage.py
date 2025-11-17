import allure
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

    @allure.step("Input data: first_name, last_name, zip_code")
    def fill_info(self, first_name: str, last_name: str,
                  zip_code: str) -> None:
        first_name_field = (self.waiter.until(EC.visibility_of_element_located
                                              (self.FIRST_NAME_LOCATOR)))
        first_name_field.send_keys(first_name)
        last_name_field = self.waiter.until(EC.visibility_of_element_located
                                            (self.LAST_NAME_LOCATOR))
        last_name_field.send_keys(last_name)
        zip_code_field = self.waiter.until(EC.visibility_of_element_located
                                           (self.ZIP_CODE_LOCATOR))
        zip_code_field.send_keys(zip_code)

    @allure.step("Press continue button")
    def continue_checkout(self) -> None:
        continue_btn = self.waiter.until(EC.element_to_be_clickable
                                         (self.CONTINUE_BTN_LOCATOR))
        continue_btn.click()

    @allure.step("Get total sum")
    def get_total_sum(self) -> str:
        total_sum_element = self.waiter.until(EC.visibility_of_element_located
                                              (self.TOTAL_SUM_LOCATOR))
        return total_sum_element.text

    @allure.step("Check if the actual sum == expected sum ")
    def check_sum(self, expected_sum, actual_total_text):
        assert expected_sum in actual_total_text, (
            f"Ошибка! Ожидаемая сумма: '{expected_sum}',"
            f"но получено: '{actual_total_text}'")
