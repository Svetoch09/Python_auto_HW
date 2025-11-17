import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage:
    INPUT_USERNAME_LOCATOR = (By.ID, "user-name")
    INPUT_PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BTN_LOCATOR = (By.ID, "login-button")

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.waiter = WebDriverWait(self.driver, 50, 0.5)

    @allure.step("Open the shop page")
    def open(self):
        self.driver.get(self.base_url)

    @allure.step("Login with creds username= {username} and "
                 "password = {password}")
    def login(self, username: str, password: str) -> None:
        user_name_field = self.waiter.until(
            EC.visibility_of_element_located(self.INPUT_USERNAME_LOCATOR))
        user_name_field.clear()
        user_name_field.send_keys(username)

        password_field = self.waiter.until(
            EC.visibility_of_element_located(self.INPUT_PASSWORD_LOCATOR))
        password_field.clear()
        password_field.send_keys(password)

        login_btn = self.waiter.until(
            EC.visibility_of_element_located(self.LOGIN_BTN_LOCATOR))
        login_btn.click()
