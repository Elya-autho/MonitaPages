from pages.BasePage import BasePage
from core.database_connection import DatabaseConnections
from selenium.webdriver.common.by import By

import allure


class LoginPageLocators:
    INPUT_PHONE = (By.XPATH, '//*[@class="login-phone-number"]')
    SEND_BUTTON_NEXT = (By.XPATH, '//*[@class="login-phone-next"]')
    INPUT_SMS_CODE = (By.XPATH, '//*[@class="login-sms-code"]')
    SEND_BUTTON_NEXT_SMS_CODE = (By.XPATH, '//*[@class="login-sms-code"]')
    CLICK_LINK_SMS_CODE =(By.XPATH, '//*[@class ="login-sms-code-again-a"]')



class LoginPageHelper(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()

        self.find_element(LoginPageLocators.INPUT_PHONE)
        self.find_element(LoginPageLocators.SEND_BUTTON_NEXT)
        self.find_element(LoginPageLocators.INPUT_SMS_CODE)
        self.find_element(LoginPageLocators.SEND_BUTTON_NEXT_SMS_CODE)
        self.find_element(LoginPageLocators.CLICK_LINK_SMS_CODE)

    @allure.step("Вводим номер телефона")
    def enter_phone(self, TEL):
        self.find_element(LoginPageLocators.INPUT_PHONE).send_keys(TEL)
        self.attach_screenshot()

    @allure.step("Нажимаем на кнопку 'Далее'")
    def send_button_next(self,):
        button_next = self.find_element(LoginPageLocators.SEND_BUTTON_NEXT)  # сохраняем элемент в переменную
        button_next.click()
        self.attach_screenshot()

    @allure.step("Вводим смс код из бд'")
    def enter_sms_code(self):
        db = DatabaseConnections()
        sms_input = self.find_element(LoginPageLocators.INPUT_SMS_CODE)
        sms_input.send_keys()

        self.attach_screenshot()

