import allure
import time
from typing import Tuple, Union
from selenium.webdriver.remote.webdriver import WebDriver

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

    def __init__(self, driver: WebDriver, base_url: str) -> None:
        """
        Инициализирует Page Object.
        :param driver: Экземпляр WebDriver.
        :param base_url: Базовый URL страницы калькулятора.
        """
        self.driver = driver
        self.base_url = base_url
        self.waiter = WebDriverWait(self.driver, 50, 0.5)

    @allure.step("Open the calculator page")
    def open(self) -> None:
        self.driver.get(self.base_url)

    @allure.step("Clear a delay field, set calculator delay ")
    def set_delay(self, delay_value: Union[int, str]) -> None:
        """"Set delay for calculator"""
        with allure.step(f"Setting delay to {delay_value} seconds"):
            delay_input_field = self.waiter.until(
                EC.visibility_of_element_located(self.DELAY_INPUT_LOCATOR)
            )
            delay_input_field.clear()
            delay_input_field.send_keys(str(delay_value))

    @allure.step("Set 7 + 8  and get start_time")
    def calculate_sum_and_get_time(self) -> Tuple[str, float]:
        """
        Выполняет операцию '7 + 8' и записывает время перед нажатием '='.
        :rtype: Tuple[str, float] - Кортеж, содержащий:
                1. Текущий текст на экране (до расчета). Тип: str.
                2. Время старта (start_time). Тип: float.

        """
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

    @allure.step("Wait untill the results field will change and get stop_time")
    def wait_for_result_change(self, pre_calc_text: str) -> float:
        """
            Ожидает изменения результата на экране и записывает время
            окончания.
            :param pre_calc_text: Текст на экране до начала расчета. Тип: str.
            :rtype: float - Время окончания операции (stop_time). Тип: float.
        """
        self.waiter.until_not(
            EC.text_to_be_present_in_element(self.RESULT_LOCATOR,
                                             pre_calc_text)
        )
        stop_time = time.time()
        return stop_time

    @allure.step("Get the result")
    def get_actual_result(self) -> str:
        """
            Получает текущий текст результата с экрана.
            :rtype: str - Фактический результат.
        """
        return self.driver.find_element(*self.RESULT_LOCATOR).text

    @allure.step("Calculate elapsed time (Stop - Start)")
    def calculate_elapsed_time(self, start_time: float,
                               stop_time: float) -> float:
        """
            Рассчитывает прошедшее время между стартом и остановкой.
            :param start_time: Время старта. Тип: float.
            :param stop_time: Время окончания. Тип: float.
            :rtype: float - Прошедшее время (elapsed_time).
        """

        elapsed_time = stop_time - start_time
        return elapsed_time

    @allure.step("Check the result")
    def assert_math_validation(self, actual_result: str,
                               expected_result: str) -> None:
        """
        Проверяет, соответствует ли фактический результат ожидаемому.
        :param actual_result: Фактический результат. Тип: str.
        :param expected_result: Ожидаемый результат. Тип: str.
        :rtype: None
        """
        assert actual_result == expected_result, \
            (f"Ожидаемый результат '{expected_result}', "
             f"но на экране '{actual_result}'")

    @allure.step("Check the delay")
    def assert_delay_validation(self, elapsed_time: float,
                                expected_delay: Union[int, str]) -> None:
        """
        Проверяет, соответствует ли прошедшее время установленной задержке.
        Ожидаемое минимальное время: expected_delay - 1.
        :param elapsed_time: Прошедшее время. Тип: float.
        :param expected_delay: Ожидаемая задержка. Тип: int или str.
        :rtype: None
        """
        expected_min_delay = int(expected_delay) - 1
        assert elapsed_time >= expected_min_delay, \
            (f"Операция выполнена слишком быстро. "
             f"Ожидалось >= {expected_min_delay} сек,"
             f"получено {elapsed_time:.2f} сек.")
