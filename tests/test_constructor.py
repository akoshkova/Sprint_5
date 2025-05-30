class TestConstructor:
    def test_constructor_sections(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/constructor")

        browser.find_element(*ConstructorLocators.BUNS_BUTTON).click()
        assert "Булки" in browser.page_source

        browser.find_element(*ConstructorLocators.SAUCES_BUTTON).click()
        assert "Соусы" in browser.page_source

        browser.find_element(*ConstructorLocators.FILLINGS_BUTTON).click()
        assert "Начинки" in browser.page_source

        browser.quit()

    def test_constructor_access_without_login(self, browser):
        browser.get("https://stellarburgers.nomoreparties.site/constructor")
        assert "Регистрация" in browser.page_source
        browser.quit()
