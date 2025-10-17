import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

INPUT_USERNAME_LOCATOR = (By.ID, "user-name")
INPUT_PASSWORD_LOCATOR = (By.ID, "password")
LOGIN_BTN_LOCATOR = (By.ID, "login-button")

ATC_BTN_BACKPACK_LOCATOR = (By.ID,
                            "add-to-cart-sauce-labs-backpack")
ATC_BTN_TSHIRT_LOCATOR = (By.ID,
                          "add-to-cart-sauce-labs-bolt-t-shirt")
ATC_BTN_ONESIE_LOCATOR = (By.ID,
                          "add-to-cart-sauce-labs-onesie")
CART_BTN_LOCATOR = (By.XPATH, "//a[@class='shopping_cart_link']")
CHECKOUT_BTN_LOCATOR = (By.XPATH, "//button[@id='checkout']")
FIRST_NAME_LOCATOR = (By.ID, "first-name")
LAST_NAME_LOCATOR = (By.ID, "last-name")
ZIP_CODE_LOCATOR = (By.ID, "postal-code")
CONTINUE_BTN_LOCATOR = (By.ID, "continue")
TOTAL_SUM_LOCATOR = (By.XPATH, "//div[@data-test='total-label']")

EXPECTED_SUM = "$58.29"


class TestAddGoodsToShoppingCart:

    def setup_method(self):
        self.driver = webdriver.Firefox(service=FirefoxService(
            GeckoDriverManager().install()))
        self.driver.get(BASE_URL)
        self.waiter = WebDriverWait(self.driver, 50, 0.5)

    def login(self):
        user_name_field = self.waiter.until(
            EC.visibility_of_element_located(INPUT_USERNAME_LOCATOR))
        user_name_field.clear()
        user_name_field.send_keys(USERNAME)

        password_field = self.waiter.until(
            EC.visibility_of_element_located(INPUT_PASSWORD_LOCATOR))
        password_field.clear()
        password_field.send_keys(PASSWORD)

        login_btn = self.waiter.until(
            EC.visibility_of_element_located(LOGIN_BTN_LOCATOR))
        login_btn.click()

    @pytest.mark.positive
    def test_sum_shopping_cart(self):
        self.login()

        # 2. Добавление товаров в корзину
        add_to_cart_backpack = self.waiter.until(EC.element_to_be_clickable
                                                 (ATC_BTN_BACKPACK_LOCATOR))
        add_to_cart_backpack.click()
        add_to_cart_tshirt = self.waiter.until(EC.element_to_be_clickable
                                               (ATC_BTN_TSHIRT_LOCATOR))
        add_to_cart_tshirt.click()
        add_to_cart_onesie = self.waiter.until(EC.element_to_be_clickable
                                               (ATC_BTN_ONESIE_LOCATOR))
        add_to_cart_onesie.click()

        # 3. Переход в корзину
        go_to_cart = self.waiter.until(EC.element_to_be_clickable
                                       (CART_BTN_LOCATOR))
        go_to_cart.click()
        # 4. Переход к оформлению (Checkout)
        check_out = self.waiter.until(EC.element_to_be_clickable
                                      (CHECKOUT_BTN_LOCATOR))
        check_out.click()
        # 5. Ввод данных покупателя
        first_name = self.waiter.until(EC.visibility_of_element_located
                                       (FIRST_NAME_LOCATOR))
        first_name.send_keys("Светлана")
        last_name = self.waiter.until(EC.visibility_of_element_located
                                      (LAST_NAME_LOCATOR))
        last_name.send_keys("Иванова")
        zip_code = self.waiter.until(EC.visibility_of_element_located
                                     (ZIP_CODE_LOCATOR))
        zip_code.send_keys("12345")
        # 6. CONTINUE
        continue_btn = self.waiter.until(EC.element_to_be_clickable
                                         (CONTINUE_BTN_LOCATOR))
        continue_btn.click()

        # 7. Проверка итоговой суммы
        actual_total_text = self.waiter.until(
            EC.visibility_of_element_located(TOTAL_SUM_LOCATOR)).text

        assert EXPECTED_SUM in actual_total_text, (
            f"Ошибка! Ожидаемая сумма: '{EXPECTED_SUM}',"
            f"но получено: '{actual_total_text}'")

    def teardown_method(self):
        """Закрывает браузер после каждого теста."""
        self.driver.quit()
