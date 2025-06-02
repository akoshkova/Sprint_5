from page_objects.locators import BaseLocators, RegistrationLocators

class TestLogin:
    def test_login_from_main(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*BaseLocators.LOGIN_BUTTON).click()

        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        assert "Личный кабинет" in browser.page_source

    def test_login_from_profile(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/profile")
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        assert "Личный кабинет" in browser.page_source



