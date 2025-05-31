import pytest
from page_objects.locators import BaseLocators, ProfileLocators, RegistrationLocators

class TestLogout:
    def test_logout(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*BaseLocators.LOGIN_BUTTON).click()
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        browser.find_element(*ProfileLocators.LOGOUT_BUTTON).click()
        assert "Войти в аккаунт" in browser.page_source
        browser.quit()
