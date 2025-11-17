import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox(service=FirefoxService(
        GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
