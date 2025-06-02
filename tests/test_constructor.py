import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.locators import ConstructorLocators


class Helpers:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://stellarburgers.nomoreparties.site/')

    def open_tab(self, locator):
        tab_button = self.driver.find_element(*locator)
        tab_button.click()

    def check_tab_content(self, content_selector, item_selector, error_message):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(content_selector)
        )

        items = self.driver.find_elements(*item_selector)
        assert len(items) > 0, error_message


class TestConstructor:
    def test_tab_switching(self, setup, tab_name, locator):
        # Находим и кликаем по кнопке таба
        setup.open_tab(locator)

        # Ждем изменения класса активного таба
        WebDriverWait(setup.driver, 10).until(
            EC.presence_of_element_located((locator[0], f"{locator[1]}.active"))
        )

        # Проверяем, что класс изменился
        active_tab = setup.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert active_tab.is_displayed(), f"Таб {tab_name} не стал активным"

    @pytest.mark.parametrize("tab_name, locator", [
        ("Булки", ConstructorLocators.BUNS_BUTTON),
        ("Соусы", ConstructorLocators.SAUCES_BUTTON),
        ("Начинки", ConstructorLocators.FILLINGS_BUTTON)
    ])
    def test_buns_tab_content(self, setup):
        setup.open_tab(ConstructorLocators.BUNS_BUTTON)
        setup.check_tab_content(
            ConstructorLocators.BUNS_CONTENT,
            ConstructorLocators.BUN_ITEM,
            "Элементы булок не найдены"
        )

    def test_sauces_tab_content(self, setup):
        setup.open_tab(ConstructorLocators.SAUCES_BUTTON)
        setup.check_tab_content(
            ConstructorLocators.SAUCES_CONTENT,
            ConstructorLocators.SAUCE_ITEM,
            "Элементы соусов не найдены"
        )

    def test_fillings_tab_content(self, setup):
        setup.open_tab(ConstructorLocators.FILLINGS_BUTTON)
        setup.check_tab_content(
            ConstructorLocators.FILLINGS_CONTENT,
            ConstructorLocators.FILLING_ITEM,
            "Элементы начинок не найдены"
        )

    def test_initial_tab_state(self, setup):
        # Проверяем, что при загрузке страницы активен первый таб
        active_tab = setup.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, "При загрузке страницы активен не первый таб"
