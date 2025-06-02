import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.registration_page import RegistrationPage
from page_objects.locators import ErrorMessages
from page_objects.locators import BaseLocators


class TestRegistration:
    def test_successful_registration(self, browser, registration_data):
        registration_page = RegistrationPage(browser)
        registration_page.register(registration_data)

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(BaseLocators.PROFILE_BUTTON)
        )

        assert "Личный кабинет" in browser.page_source

    @pytest.mark.parametrize("name, email, password, error_message", [
        ("", "empty@test.com", "Qwerty123", "Это поле обязательно"),  # Пустое имя
        ("Аля", "invalidemail", "Qwerty123", "Неверный формат email"),  # Неверный email
        ("Аля", "alia_koshkova_22@yandex.ru", "123", "Минимальная длина пароля 6 символов")  # Короткий пароль
    ])
    def test_registration_errors(self, browser, name, email, password, error_message):
        registration_page = RegistrationPage(browser)
        registration_page.open()
        registration_page.click_register_button()

        registration_page.fill_registration_form(name, email, password)
        registration_page.click_register_button()

        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(ErrorMessages.REGISTRATION_ERROR)
        )

        assert error_message in browser.page_source

    def test_registration_with_existing_email(self, browser, registration_data):
        # Первая регистрация
        registration_page = RegistrationPage(browser)
        registration_page.register(registration_data)

        # Попытка повторной регистрации
        registration_page.open()
        registration_page.click_register_button()

        registration_page.fill_registration_form("Аля", registration_data['email'], registration_data['password'])
        registration_page.click_register_button()

        assert "Пользователь с таким email уже существует" in browser.page_source
