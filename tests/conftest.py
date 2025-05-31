import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from generator_data import generate_email, generate_password

@pytest.fixture(scope="session")
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Фикстура для ожидания элементов
@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)

# Фикстура для конструктора
@pytest.fixture
def constructor_page(browser):
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser

# Фикстура для пользовательских данных
@pytest.fixture
def registration_data():
    return {
        "email": generate_email(),
        "password": generate_password()
    }