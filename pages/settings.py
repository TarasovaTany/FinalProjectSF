"""Тестовые данные"""

from faker import Faker
import string

base_url = "https://b2c.passport.rt.ru"
"""Базовый URL тестируемого сайта РосТелеКом"""

# Валидные данные:
valid_email = "pro100test.testing@yandex.ru"
valid_password = 'Qwerty147'
valid_firstname = "Ирина"
valid_lastname = "Петрова"
valid_login = "administrator123"
valid_region = "Воронежская обл"

# Невалидные данные:
random = Faker()

# Случайный пароль:
random_password = random.password()
# Случайный адрес электронной почты:
random_email = random.email()

invalid_ls = "123456789012"
invalid_login = "administrator"
invalid_phone = "+37594568321"

def generate_string_rus(n):
    return 'ф' * n   # генерация строки из букв на кириллице
def generate_string_en(n):
    return "f" * n   # генерация строки из букв на латинице
def english_chars():
    return 'zxcvbnmasdfghjklqwertyuiop'   # английский алфавит
def russian_chars():
    return 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'   # русский алфавит
def special_chars():
    return f'{string.punctuation}'  # специальные симовлы
def chinese_symbols():  # популярные китайсике иероглифы
    return '龍門大酒家'