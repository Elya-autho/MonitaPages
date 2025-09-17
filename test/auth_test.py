import allure
from core.base_test import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageLocators, LoginPageHelper
import time


BASE_URL ="https://test.kb-monita.ru/#monitorings_exclude"
TEL = 9085728301
@allure.feature("Тесты BasePage")
@allure.story("Проверка открытия страницы")
def test_get_url(browser):
    """
    Тест проверяет, что метод get_url корректно открывает указанный URL
    """
    with allure.step("Инициализируем BasePage"):
        base_page = BasePage(browser)

    with allure.step("Открываем тестовую страницу"):
        base_page.get_url(BASE_URL)
    time.sleep(5)

@allure.story("Проверка ввода номера телефона")
def test_input_phone(browser):
    with allure.step("Открываем страницу"):
        BasePage(browser).get_url(BASE_URL)
    with allure.step("Создаем объект страницы"):
        input_phone = LoginPageHelper(browser)
    with allure.step("Вводим номер телефона"):
        input_phone.enter_phone(TEL)
    time.sleep(10)

@allure.story("Проверка клика по кнопке 'Далее'")
def test_input_ph(browser):
    with allure.step("Открываем страницу"):
        BasePage(browser).get_url(BASE_URL)
    with allure.step("Создаем объект страницы"):
        input_phone = LoginPageHelper(browser)
    with allure.step("Вводим номер телефона"):
        input_phone.enter_phone(TEL)
    with allure.step("Создаем объект страницы"):
        send_next = LoginPageHelper(browser)
    with allure.step("Нажимаем на кнопку Далее"):
        send_next.send_button_next()
        time.sleep(20)

@allure.story("Проверка ввода кода из смс")
def test_input_sms_code(browser):
    with allure.step("Открываем страницу"):
        BasePage(browser).get_url(BASE_URL)
    with allure.step("Создаем объект страницы"):
        input_phone = LoginPageHelper(browser)
    with allure.step("Вводим номер телефона"):
        input_phone.enter_phone(TEL)
    with allure.step("Создаем объект страницы"):
        send_next = LoginPageHelper(browser)
    with allure.step("Нажимаем на кнопку Далее"):
        send_next.send_button_next()
        time.sleep(20)
    with allure.step("Вводим смс код"):
        enter_sms_code = LoginPageHelper(browser)  # Создаем объект страницы
        enter_sms_code.enter_sms_code()
        time.sleep(10)
    with allure.step("Создаем объект страницы"):
        send_next_after_sms = LoginPageHelper(browser)
    with allure.step("Нажимаем на кнопку 'Далее' после ввода смс кода"):
        send_next_after_sms.send_button_next_after_sms()

