import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.locators import ConstructorLocators
from page_objects.constructor_page import ConstructorPage


class TestConstructor:
    def test_tab_switching(self, setup, tab_name, locator):
        constructor = ConstructorPage(setup.driver)
        constructor.open_tab(locator)

        WebDriverWait(setup.driver, 10).until(
            EC.presence_of_element_located((locator[0], f"{locator[1]}.active"))
        )

        active_tab = setup.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert active_tab.is_displayed(), f"Таб {tab_name} не стал активным"

    @pytest.mark.parametrize("tab_name, locator", [
        ("Булки", ConstructorLocators.BUNS_BUTTON),
        ("Соусы", ConstructorLocators.SAUCES_BUTTON),
        ("Начинки", ConstructorLocators.FILLINGS_BUTTON)
    ])
    def test_buns_tab_content(self, setup):
        constructor = ConstructorPage(setup.driver)
        constructor.open_tab(ConstructorLocators.BUNS_BUTTON)
        constructor.check_tab_content(
            ConstructorLocators.BUNS_CONTENT,
            ConstructorLocators.BUN_ITEM,
            "Элементы булок не найдены"
        )

    def test_sauces_tab_content(self, setup):
        constructor = ConstructorPage(setup.driver)
        constructor.open_tab(ConstructorLocators.SAUCES_BUTTON)
        constructor.check_tab_content(
            ConstructorLocators.SAUCES_CONTENT,
            ConstructorLocators.SAUCE_ITEM,
            "Элементы соусов не найдены"
        )

    def test_fillings_tab_content(self, setup):
        constructor = ConstructorPage(setup.driver)
        constructor.open_tab(ConstructorLocators.FILLINGS_BUTTON)
        constructor.check_tab_content(
            ConstructorLocators.FILLINGS_CONTENT,
            ConstructorLocators.FILLING_ITEM,
            "Элементы начинок не найдены"
        )

    def test_initial_tab_state(self, setup):
        active_tab = setup.driver.find_element(*ConstructorLocators.ACTIVE_TAB)
        assert "Булки" in active_tab.text, "При загрузке страницы активен не первый таб"
