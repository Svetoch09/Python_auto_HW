import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class FormPage:
    ALL_INPUTS_LOCATOR = (By.CSS_SELECTOR, "input.form-control")
    SUBMIT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[type='submit']")
    ALL_ALERTS_LOCATOR = (By.CSS_SELECTOR, "div.alert")

    SUCCESS_CLASS = "alert-success"  # Зеленый
    DANGER_CLASS = "alert-danger"  # Красный (для Zip code)

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.waiter = WebDriverWait(self.driver, 10, 0.5)

    @allure.step("Open a form page")
    def open(self) -> None:
        self.driver.get(self.base_url)  # open page

    @allure.step("Input data into fields form page")
    def fill_all_fields(self, data_list: list) -> None:
        input_fields = self.waiter.until(
            EC.visibility_of_all_elements_located(self.ALL_INPUTS_LOCATOR)
        )
        for i, field in enumerate(input_fields):
            field.send_keys(data_list[i])

    @allure.step("Press SUBMIT button")
    def submit_form(self) -> None:
        submit_button = self.waiter.until(
            EC.element_to_be_clickable(self.SUBMIT_BUTTON_LOCATOR)
        )
        submit_button.click()

    @allure.step("Get all alerts")
    def get_alert_fields(self) -> list:
        """Возвращает список элементов-алертов (результатов валидации)."""
        return self.waiter.until(
            EC.visibility_of_all_elements_located(self.ALL_ALERTS_LOCATOR)
        )

    @allure.step("Check alerts")
    def assert_validation_colors(self, danger_index):
        alert_fields = self.get_alert_fields()  # все элементы-алерты

        for i, alert in enumerate(alert_fields):
            if i == danger_index:
                expected_class = self.DANGER_CLASS  # Красный
            else:
                expected_class = self.SUCCESS_CLASS  # Зеленый

            actual_classes = alert.get_attribute("class")

            assert expected_class in actual_classes, \
                (f"Ошибка валидации поля {i} (CSS-класс):"
                 f"Ожидался класс '{expected_class}',"
                 f"но найдены: '{actual_classes}'")
