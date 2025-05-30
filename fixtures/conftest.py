from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import random
import string


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{username}@test.com"


def generate_password():
    # Генерация пароля из 8 символов:
    # - минимум 1 заглавная буква
    # - минимум 1 цифра
    # - минимум 1 специальный символ
    # - остальные символы - строчные буквы

    password_chars = [
        random.choice(string.ascii_uppercase),  # заглавная буква
        random.choice(string.digits),  # цифра
        random.choice('!@#$%^&*()_+'),  # специальный символ
        ''.join(random.choices(string.ascii_lowercase, k=5))  # оставшиеся символы
    ]

    # Перемешиваем символы для большей случайности
    random.shuffle(password_chars)
    return ''.join(password_chars)


# Альтернативная версия генератора паролей с параметром длины
def generate_password_with_length(length=8):
    if length < 6:
        raise ValueError("Минимальная длина пароля - 6 символов")

    password_chars = [
        random.choice(string.ascii_uppercase),  # заглавная буква
        random.choice(string.digits),  # цифра
        random.choice('!@#$%^&*()_+'),  # специальный символ
        ''.join(random.choices(string.ascii_lowercase + string.digits + '!@#$%^&*()_+', k=length - 3))
    ]

    random.shuffle(password_chars)
    return ''.join(password_chars)
