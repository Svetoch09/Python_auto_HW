import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

EDGE_DRIVER_PATH = r"D:\Program Files\Edgedriver\msedgedriver.exe"
BASE_URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
ALL_INPUTS_LOCATOR = (By.CSS_SELECTOR, "input.form-control")
SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[type='submit']")
ALL_ALERTS_LOCATOR = (By.CSS_SELECTOR, "div.alert")

SUCCESS_CLASS = "alert-success"   # Зеленый
DANGER_CLASS = "alert-danger"   # Красный (для Zip code)

INPUT_DATA = [
    "Иван", "Петров", "Ленина, 55-3", "", "Москва",
    "Россия", "test@skypro.com", "+7985899998787", "QA", "SkyPro"
]


class TestDataFormValidation:

    def setup_method(self):
        """Инициализирует драйвер и открывает страницу."""
        edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
        self.driver = webdriver.Edge(service=edge_service)
        self.driver.get(BASE_URL)
        self.waiter = WebDriverWait(self.driver, 10, 0.5)

    @pytest.mark.negative
    def test_data_validation_after_submit(self):
        input_fields = self.waiter.until(
            EC.visibility_of_all_elements_located(ALL_INPUTS_LOCATOR)
        )
        for i, field in enumerate(input_fields):
            field.send_keys(INPUT_DATA[i])

        submit_button = self.waiter.until(
            EC.element_to_be_clickable(SUBMIT_BUTTON_LOCATOR)
        )
        submit_button.click()

        alert_fields = self.waiter.until(
            EC.visibility_of_all_elements_located(ALL_ALERTS_LOCATOR)
        )

        for i, alert in enumerate(alert_fields):
            if i == 3:
                expected_class = DANGER_CLASS
            else:
                expected_class = SUCCESS_CLASS    # поля ожидаются как зеленые

            actual_classes = alert.get_attribute("class")

            assert expected_class in actual_classes, \
                (f"Ошибка валидации поля {i}:"
                 f"Ожидался класс '{expected_class}',"
                 f"но найдены: '{actual_classes}'")

    def teardown_method(self):
        """Закрывает браузер после каждого теста."""
        self.driver.quit()
