from selenium.webdriver.common.by import By

class BaseLocators:
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".auth__button_login")  # Кнопка входа
    PROFILE_BUTTON = (By.CSS_SELECTOR, ".profile")  # Кнопка профиля
    CONSTRUCTOR_BUTTON = (By.CSS_SELECTOR, ".constructor")  # Кнопка конструктора
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".auth__button_registration")  # Кнопка регистрации
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".auth__password_reset")  # Кнопка восстановления пароля

class RegistrationLocators:
    NAME_INPUT = (By.ID, "name")  # Поле имени
    EMAIL_INPUT = (By.ID, "email")  # Поле email
    PASSWORD_INPUT = (By.ID, "password")  # Поле пароля
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".registration__button")  # Кнопка регистрации

class ProfileLocators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".profile__button_logout")  # Кнопка выхода

class ConstructorLocators:
    # Локаторы для вкладок
    BUNS_BUTTON = (By.CSS_SELECTOR, ".tabs__tab_buns")  # Кнопка булок
    SAUCES_BUTTON = (By.CSS_SELECTOR, ".tabs__tab_sauces")  # Кнопка соусов
    FILLINGS_BUTTON = (By.CSS_SELECTOR, ".tabs__tab_fillings")  # Кнопка начинок

    # Локаторы для контента вкладок
    BUNS_CONTENT = (By.CSS_SELECTOR, ".buns")  # Контент-блок с булками
    SAUCES_CONTENT = (By.CSS_SELECTOR, ".sauces")  # Контент-блок с соусами
    FILLINGS_CONTENT = (By.CSS_SELECTOR, ".fillings")  # Контент-блок с начинками

    # Локаторы для элементов контента
    BUN_ITEM = (By.CSS_SELECTOR, ".ingredient")  # Элемент списка булок
    SAUCE_ITEM = (By.CSS_SELECTOR, ".ingredient")  # Элемент списка соусов
    FILLING_ITEM = (By.CSS_SELECTOR, ".ingredient")  # Элемент списка начинок

    # Общий локатор для активного таба
    ACTIVE_TAB = (By.CSS_SELECTOR, ".tabs__tab_active")  # Активный таб на странице

class ErrorMessages:
    EMPTY_NAME_ERROR = (By.CSS_SELECTOR, ".input__error")  # Ошибка пустого имени
    INVALID_EMAIL_ERROR = (By.CSS_SELECTOR, ".input__error")  # Ошибка неверного email
    SHORT_PASSWORD_ERROR = (By.CSS_SELECTOR, ".input__error")  # Ошибка короткого пароля
    REGISTRATION_ERROR = (By.CSS_SELECTOR, ".input__error")
