import pytest
import allure
from base_test import browser
from pages.BasePage import BasePage
from pages.ExceptionPage import ExceptionPageLocators
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

    with allure.step("Открываем тестовую страницу"):
        base_page.auth(TEL)
    time.sleep(10)