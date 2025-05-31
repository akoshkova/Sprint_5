from selenium.webdriver.common.by import By

class BaseLocators:
    # Основные элементы главной страницы
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка входа
    PROFILE_BUTTON = (By.XPATH, "//button[contains(text(), 'Личный кабинет')]")  # Кнопка профиля
    CONSTRUCTOR_BUTTON = (By.XPATH, "//button[contains(text(), 'Конструктор')]")  # Кнопка конструктора
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Регистрация')]")  # Кнопка регистрации
    FORGOT_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")  # Кнопка восстановления пароля

class RegistrationLocators:
    # Форма регистрации
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Имя']")  # Поле имени
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Логин']")  # Поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")  # Поле пароля
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Регистрация')]")  # Кнопка регистрации

class ProfileLocators:
    # Личный кабинет
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")  # Кнопка выхода

class ConstructorLocators:
    # Конструктор
    BUNS_BUTTON = (By.CSS_SELECTOR, ".buns-button") # Кнопка булок
    SAUCES_BUTTON = (By.CSS_SELECTOR, ".sauces-button") # Кнопка соусов
    FILLINGS_BUTTON = (By.CSS_SELECTOR, ".fillings-button") # Кнопка начинок

class ErrorMessages:
    # Сообщения об ошибках
    EMPTY_NAME_ERROR = (By.XPATH, "//p[contains(text(), 'Это поле обязательно')]")  # Ошибка пустого имени
    INVALID_EMAIL_ERROR = (By.XPATH, "//p[contains(text(), 'Неверный формат email')]")  # Ошибка неверного email
    SHORT_PASSWORD_ERROR = (By.XPATH, "//p[contains(text(), 'Минимальная длина пароля 6 символов')]")  # Ошибка короткого пароля


