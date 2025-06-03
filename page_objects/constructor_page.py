from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConstructorPage:
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
