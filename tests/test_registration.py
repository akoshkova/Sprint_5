import pytest
from page_objects.locators import RegistrationLocators
from generator_data import generate_email, generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


# Фикстура для браузера
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Неявное ожидание
    yield driver
    driver.quit()


@pytest.fixture
def registration_data():
    return {
        "email": generate_email(),
        "password": generate_password()
    }


def register_user(browser, registration_data):
    browser.get("https://stellarburgers.nomoreparties.site/")
    browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    browser.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Аля")
    browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(registration_data['email'])
    browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(registration_data['password'])
    browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()


class TestRegistration:
    def test_successful_registration(self, browser, registration_data):
        register_user(browser, registration_data)

        # Добавляем явное ожидание
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".profile"))
        )

        assert "Личный кабинет" in browser.page_source

    @pytest.mark.parametrize("name, email, password, error_message", [
        ("", "empty@test.com", "Qwerty123", "Это поле обязательно"),  # Пустое имя
        ("Аля", "invalidemail", "Qwerty123", "Неверный формат email"),  # Неверный email
        ("Аля", "alia_koshkova_22@yandex.ru", "123", "Минимальная длина пароля 6 символов")  # Короткий пароль
    ])
    def test_registration_errors(self, browser, name, email, password, error_message):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        browser.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        # Добавляем явное ожидание сообщения об ошибке
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message"))
        )

        assert error_message in browser.page_source

    def test_registration_with_existing_email(self, browser, registration_data):
        # Первая регистрация
        register_user(browser, registration_data)

        # Попытка повторной регистрации
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        browser.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Аля")
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(registration_data['email'])
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(registration_data['password'])
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        assert "Пользователь с таким email уже существует" in browser.page_source

