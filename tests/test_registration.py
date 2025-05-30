class TestRegistration:
    def test_successful_registration(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/")
        browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

        browser.find_element(*RegistrationLocators.NAME_INPUT).send_keys("Аля")
        browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys("alia_koshkova_22@yandex.ru")
        browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys("Qwerty123")
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        assert "Личный кабинет" in browser.page_source
        browser.quit()

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
        browser.find_element(*RegistrationLocators.REGISTER_SUBMIT).click()

        assert error_message in browser.page_source
        browser.quit()
