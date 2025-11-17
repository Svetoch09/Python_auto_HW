import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

EDGE_DRIVER_PATH = r"D:\Program Files\Edgedriver\msedgedriver.exe"
BASE_URL = ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="function")
def driver():
    """Инициализирует драйвер и открывает страницу."""
    edge_service = EdgeService(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=edge_service)

    yield driver
    driver.quit()
