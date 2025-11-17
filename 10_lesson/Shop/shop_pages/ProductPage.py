import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ProductPage:
    ATC_BTN_BACKPACK_LOCATOR = (By.ID,
                                "add-to-cart-sauce-labs-backpack")
    ATC_BTN_TSHIRT_LOCATOR = (By.ID,
                              "add-to-cart-sauce-labs-bolt-t-shirt")
    ATC_BTN_ONESIE_LOCATOR = (By.ID,
                              "add-to-cart-sauce-labs-onesie")
    CART_BTN_LOCATOR = (By.XPATH, "//a[@class='shopping_cart_link']")

    def __init__(self, driver):
        self.driver = driver
        self.waiter = WebDriverWait(self.driver, 10)

    @allure.step("Add goods into a cart")
    def add_to_cart(self) -> None:
        add_to_cart_backpack = self.waiter.until(EC.element_to_be_clickable
                                                 (self.
                                                  ATC_BTN_BACKPACK_LOCATOR))
        add_to_cart_backpack.click()

        add_to_cart_tshirt = self.waiter.until(EC.element_to_be_clickable
                                               (self.ATC_BTN_TSHIRT_LOCATOR))
        add_to_cart_tshirt.click()

        add_to_cart_onesie = self.waiter.until(EC.element_to_be_clickable
                                               (self.ATC_BTN_ONESIE_LOCATOR))
        add_to_cart_onesie.click()

    @allure.step("Go to the shopping cart page")
    def go_to_cart(self):
        go_to_cart = self.waiter.until(EC.element_to_be_clickable
                                       (self.CART_BTN_LOCATOR))
        go_to_cart.click()
