import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from generator_data import generate_email, generate_password, generate_name


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    driver = None

    try:
        if browser_name == "chrome":
            options = Options()
            options.add_argument("--start-maximized")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Браузер {browser_name} не поддерживается")

        yield driver

    finally:
        if driver:
            driver.quit()

@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)

@pytest.fixture
def registration_data():
    return {
        "name": generate_name(),
        "email": generate_email(),
        "password": generate_password()
    }
