import pytest
from pages.auth_page import *
from pages.settings import *
import time


"""Негативный сценарий восстановления пароля по адресу электронной почты. Невалидный адрес электронной почты"""
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_email(browser):
    page = NewPassPage(browser)
    page.enter_username(random_email)   # вводим невалидный адрес эл. почты
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной ввод капчи
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"


"""Негативный сценарий восстановления пароля по номеру телефона. Невалидный номер мобильного телефона"""
@pytest.mark.newpass
@pytest.mark.negative
def test_new_pass_wrong_phone(browser):
    page = NewPassPage(browser)
    page.enter_username(invalid_phone)   # вводим невалидный номер мобильного телефона
    browser.implicitly_wait(10)
    time.sleep(30)  # время на ручной ввод капчи
    page.btn_continue.click()

    error_mess = browser.find_element(*AuthLocators.AUTH_FORM_ERROR)
    assert error_mess.text == "Неверный логин или текст с картинки"
