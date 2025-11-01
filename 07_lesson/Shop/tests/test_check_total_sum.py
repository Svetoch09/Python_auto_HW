import pytest
from Shop.shop_pages.LoginPage import LoginPage
from Shop.shop_pages.ProductPage import ProductPage
from Shop.shop_pages.CartPage import CartPage
from Shop.shop_pages.CheckoutPage import CheckoutPage

EXPECTED_SUM = "$58.29"

username = "standard_user"
password = "secret_sauce"
first_name = "Svetlana"
last_name = "Ivanova"
zip_code = "12345"


class TestCheckTotalSum:

    @pytest.mark.positive
    def test_check_total_sum(self, driver, base_url):
        """ Тест проверяет корректность суммы заказа """
        login_page = LoginPage(driver, base_url)
        login_page.open()
        login_page.login(username, password)

        product_page = ProductPage(driver)
        product_page.add_to_cart()
        product_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_info(first_name, last_name, zip_code)
        checkout_page.continue_checkout()
        actual_total_text = checkout_page.get_total_sum()
        checkout_page.check_sum(EXPECTED_SUM, actual_total_text)
