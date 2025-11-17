import allure
import pytest

from Calculator.calculator_pages.SlowCalculatorPage import SlowCalculatorPage
from selenium.webdriver.remote.webdriver import WebDriver

EXPECTED_RESULT = "15"
EXPECTED_DELAY = "45"  # delay


@allure.parent_suite("Lesson 7")
@allure.suite("Калькулятор")
class TestSlowCalculator:
    """Класс для тестирования медленного калькулятора."""

    @allure.id("Calculator-1")
    @allure.feature("Установка времени задержки пользователем.")
    @allure.title("Test. Установка задержки и проверка корректности "
                  "работы калькулятора")
    @allure.description("""Проверка корректности работы калькулятора,
                            а также проверка задержки вермени""")
    @allure.severity("NORMAL")
    @pytest.mark.positive
    def test_sum_result_with_delay(self, driver: WebDriver,
                                   base_url: str) -> None:
        """
            Тест: Проверяет сумму 7+8 и фактическое время выполнения,
            сравнивая его с заданной задержкой.
            :param driver: Экземпляр WebDriver, предоставляемый фикстурой.
            Тип: WebDriver.
            :param base_url: Базовый URL страницы, предоставляемый фикстурой.
            Тип: str.
            :rtype: None
        """
        page = SlowCalculatorPage(driver, base_url)
        page.open()
        page.set_delay(EXPECTED_DELAY)

        pre_calc_text_dynamic, start_time = page.calculate_sum_and_get_time()
        end_time = page.wait_for_result_change(pre_calc_text_dynamic)
        elapsed_time = page.calculate_elapsed_time(start_time, end_time)

        actual_result = page.get_actual_result()

        page.assert_math_validation(
            actual_result, EXPECTED_RESULT)

        page.assert_delay_validation(
            elapsed_time, EXPECTED_DELAY)
