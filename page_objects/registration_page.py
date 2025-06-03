from page_objects.locators import RegistrationLocators

class RegistrationPage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get("https://stellarburgers.nomoreparties.site/")

    def click_register_button(self):
        self.browser.find_element(*RegistrationLocators.REGISTER_BUTTON).click()

    def fill_registration_form(self, name, email, password):
        self.browser.find_element(*RegistrationLocators.NAME_INPUT).send_keys(name)
        self.browser.find_element(*RegistrationLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*RegistrationLocators.PASSWORD_INPUT).send_keys(password)

    def register(self, registration_data):
        self.open()
        self.click_register_button()
        self.fill_registration_form(
            registration_data['name'],
            registration_data['email'],
            registration_data['password']
        )
        self.click_register_button()
