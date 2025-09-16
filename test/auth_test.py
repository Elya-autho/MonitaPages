import allure
from core.base_test import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
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

    with allure.step("Вводим номер телефона"):
        input_phone = LoginPageHelper(browser)  # Создаем объект страницы
        input_phone.enter_phone(TEL)
        time.sleep(20)

    with allure.step("Нажимаем на кнопку 'Далее'"):
        send_ = LoginPageHelper(browser)  # Создаем объект страницы
        send_.send_button_next()
        time.sleep(20)

    with allure.step("Вводим смс код"):
        login_page = LoginPageHelper(browser)  # Создаем объект страницы
        login_page.enter_phone(TEL)
        time.sleep(20)