import pytest
import time

from Calculator.calculator_pages.SlowCalculatorPage import SlowCalculatorPage

EXPECTED_RESULT = "15"
EXPECTED_DELAY = "15"  # delay


class TestSlowCalculator:
    """Класс для тестирования медленного калькулятора."""

    @pytest.mark.positive
    def test_sum_result_with_delay(self, driver, base_url):
        page = SlowCalculatorPage(driver, base_url)
        page.open()
        page.set_delay(EXPECTED_DELAY)

        pre_calc_text_dynamic, start_time = page.calculate_sum_and_get_time()
        page.wait_for_result_change(pre_calc_text_dynamic)
        end_time = time.time()
        actual_result = page.get_actual_result()
        elapsed_time = end_time - start_time

        page.assert_math_validation(
            actual_result, EXPECTED_RESULT)

        page.assert_delay_validation(
            elapsed_time, EXPECTED_DELAY)
