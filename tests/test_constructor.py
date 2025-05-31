import pytest
from page_objects.locators import ConstructorLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestConstructor:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.browser.get('https://stellarburgers.nomoreparties.site/')

    @pytest.mark.parametrize("tab_name, locator", [
        ("Булки", ConstructorLocators.BUNS_BUTTON),
        ("Соусы", ConstructorLocators.SAUCES_BUTTON),
        ("Начинки", ConstructorLocators.FILLINGS_BUTTON)
        ])
    def test_tab_switching(self, tab_name, locator):
        # Находим и кликаем по кнопке таба
        tab_button = self.browser.find_element(*locator)
        tab_button.click()

        # Ждем изменения класса активного таба
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"{locator[1]}.active"))
        )
        # Проверяем, что класс изменился
        active_tab = self.browser.find_element(By.CSS_SELECTOR, f"{locator[1]}.active")
        assert active_tab.is_displayed(), f"Таб {tab_name} не стал активным"

    def test_buns_tab_content(self):
        self.open_tab(ConstructorLocators.BUNS_BUTTON)
        self.check_tab_content(".bun-content", ".bun-item", "Элементы булок не найдены")

    def test_sauces_tab_content(self):
        self.open_tab(ConstructorLocators.SAUCES_BUTTON)
        self.check_tab_content(".sauce-content", ".sauce-item", "Элементы соусов не найдены")

    def test_fillings_tab_content(self):
        self.open_tab(ConstructorLocators.FILLINGS_BUTTON)
        self.check_tab_content(".filling-content", ".filling-item", "Элементы начинок не найдены")

    def test_initial_tab_state(self):
        # Проверяем, что при загрузке страницы активен первый таб
        active_tab = self.browser.find_element(By.CSS_SELECTOR, ".tab.active")
        assert "Булки" in active_tab.text, "При загрузке страницы активен не первый таб"

    def open_tab(self, locator):
        tab_button = self.browser.find_element(*locator)
        tab_button.click()

    def check_tab_content(self, content_selector, item_selector, error_message):
        # Ждем появления контента
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, content_selector))
        )

        # Проверяем наличие элементов
        items = self.browser.find_elements(By.CSS_SELECTOR, item_selector)
        assert len(items) > 0, error_message


