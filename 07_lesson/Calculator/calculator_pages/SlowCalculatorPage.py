import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    DELAY_INPUT_LOCATOR = (By.CSS_SELECTOR, "#delay")
    NUMBER_7_LOCATOR = (By.XPATH, "//span[text() = '7']")
    NUMBER_8_LOCATOR = (By.XPATH, "//span[text() = '8']")
    PLUS_LOCATOR = (By.XPATH, "//span[text() = '+']")
    EQUAL_LOCATOR = (By.XPATH, "//span[text() = '=']")
    RESULT_LOCATOR = (By.XPATH, "//div[@class = 'screen']")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.waiter = WebDriverWait(self.driver, 50, 0.5)

    def open(self):
        self.driver.get(self.base_url)

    def set_delay(self, delay_value):
        delay_input_field = self.waiter.until(
            EC.visibility_of_element_located(self.DELAY_INPUT_LOCATOR)
        )
        delay_input_field.clear()
        delay_input_field.send_keys(delay_value)

    def calculate_sum_and_get_time(self):
        num1 = self.waiter.until(
            EC.element_to_be_clickable(self.NUMBER_7_LOCATOR))
        num1.click()

        plus = self.waiter.until(
            EC.element_to_be_clickable(self.PLUS_LOCATOR))
        plus.click()

        num2 = self.waiter.until(
            EC.element_to_be_clickable(self.NUMBER_8_LOCATOR))
        num2.click()

        pre_calc_text_dynamic = (self.driver.find_element(*self.RESULT_LOCATOR)
                                 .text)
        # Получаем время перед нажатием "="
        start_time = time.time()
        equal = self.waiter.until(
            EC.element_to_be_clickable(self.EQUAL_LOCATOR))
        equal.click()
        return pre_calc_text_dynamic, start_time

    def wait_for_result_change(self, pre_calc_text):
        self.waiter.until_not(
            EC.text_to_be_present_in_element(self.RESULT_LOCATOR,
                                             pre_calc_text)
        )

    def get_actual_result(self):
        return self.driver.find_element(*self.RESULT_LOCATOR).text

    def assert_math_validation(self, actual_result, expected_result):
        assert actual_result == expected_result, \
            (f"Ожидаемый результат '{expected_result}', "
             f"но на экране '{actual_result}'")

    def assert_delay_validation(self, elapsed_time, expected_delay):
        expected_min_delay = int(expected_delay) - 1
        assert elapsed_time >= expected_min_delay, \
            (f"Операция выполнена слишком быстро. "
             f"Ожидалось >= {expected_min_delay} сек,"
             f"получено {elapsed_time:.2f} сек.")
