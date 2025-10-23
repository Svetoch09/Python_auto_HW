import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator."
            "html")
# Локатор поля ввода задержки
DELAY_INPUT_LOCATOR = (By.CSS_SELECTOR, "#delay")
# Локаторы кнопок калькулятора
NUMBER_7_LOCATOR = (By.XPATH, "//span[text() = '7']")
NUMBER_8_LOCATOR = (By.XPATH, "//span[text() = '8']")
PLUS_LOCATOR = (By.XPATH, "//span[text() = '+']")
EQUAL_LOCATOR = (By.XPATH, "//span[text() = '=']")
# Локатор экрана результата
RESULT_LOCATOR = (By.XPATH, "//div[@class = 'screen']")

# Ожидаемый результат и задержка
EXPECTED_RESULT = "15"
EXPECTED_DELAY = "45"  # задержка секунд


class TestSlowCalculator:
    """Класс для тестирования медленного калькулятора."""

    def setup_method(self):
        """
        Инициализирует драйвер Chrome, используя менеджер драйверов.
        Устанавливает явное ожидание (WebDriverWait).
        """
        # 1. Инициализация драйвера:
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        # 2. Открытие страницы:
        self.driver.get(BASE_URL)
        # 3. Инициализация явного ожидания:
        # Максимальное время ожидания 50 секунд - операция займет 45 секунд.
        self.waiter = WebDriverWait(self.driver, 50, 0.5)

    @pytest.mark.positive
    def test_sum_result_with_delay(self):
        # Ожидаем, пока поле ввода задержки станет видимым
        delay_input_field = self.waiter.until(
            EC.visibility_of_element_located(DELAY_INPUT_LOCATOR)
        )
        # Очищаем поле и вводим нужное значение задержки
        delay_input_field.clear()
        delay_input_field.send_keys(EXPECTED_DELAY)
        #   7 + 8
        num1 = self.waiter.until(
            EC.element_to_be_clickable(NUMBER_7_LOCATOR)
        )
        num1.click()

        plus = self.waiter.until(
            EC.element_to_be_clickable(PLUS_LOCATOR)
        )
        plus.click()

        num2 = self.waiter.until(
            EC.element_to_be_clickable(NUMBER_8_LOCATOR)
        )
        num2.click()
        # сохраняем что в поле калькулятора было введено
        pre_calc_text_dynamic = self.driver.find_element(*RESULT_LOCATOR).text
        # Получаем время перед нажатием "="
        start_time = time.time()
        #  =
        equal = self.waiter.until(
            EC.element_to_be_clickable(EQUAL_LOCATOR)
        )
        equal.click()

        # Ждем, пока текст в поле результата изменится
        self.waiter.until_not(
            EC.text_to_be_present_in_element(RESULT_LOCATOR, pre_calc_text_dynamic)
        )
        end_time = time.time()
        # Получаем фактическую строку из поля результата
        actual_result = self.driver.find_element(*RESULT_LOCATOR).text

        # Проверка корректности результата
        assert actual_result == EXPECTED_RESULT, \
            (f"Ожидаемый результат '{EXPECTED_RESULT}', "
             f"но на экране '{actual_result}'")

        #  Проверка времени выполнения
        # Время должно быть >= 44 секунд (45 - 1 сек погрешности)
        elapsed_time = end_time - start_time
        expected_min_delay = int(EXPECTED_DELAY) - 1

        assert elapsed_time >= expected_min_delay, \
            (f"Операция выполнена слишком быстро. "
             f"Ожидалось >= {expected_min_delay} сек,"
             f"получено {elapsed_time:.2f} сек.")

    def teardown_method(self):
        """Закрывает браузер после каждого теста."""
        self.driver.quit()
