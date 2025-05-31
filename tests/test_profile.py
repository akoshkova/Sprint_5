import pytest
from page_objects.locators import BaseLocators, RegistrationLocators

class TestProfile:
    def test_profile_access(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*BaseLocators.LOGIN_BUTTON).click()
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        browser.find_element(*BaseLocators.PROFILE_BUTTON).click()
        assert "Личный кабинет" in browser.page_source
        browser.quit()

    def test_constructor_access(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*BaseLocators.LOGIN_BUTTON).click()
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        browser.find_element(*BaseLocators.CONSTRUCTOR_BUTTON).click()
        assert "Конструктор" in browser.page_source
        browser.quit()

    def test_profile_to_constructor(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*BaseLocators.LOGIN_BUTTON).click()
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        browser.find_element(*BaseLocators.PROFILE_BUTTON).click()
        browser.find_element(*BaseLocators.CONSTRUCTOR_BUTTON).click()
        assert "Конструктор" in browser.page_source
        browser.quit()
