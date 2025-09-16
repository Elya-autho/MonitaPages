from pages.BasePage import BasePage

from selenium.webdriver.common.by import By
import allure


class LoginPageLocators:
    INPUT_PHONE = (By.XPATH, '//*[@class="login-phone-number"]')
    SEND_BUTTON_NEXT = (By.XPATH, '//*[@class="login-phone-next"]')



class LoginPageHelper(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()

        self.find_element(LoginPageLocators.INPUT_PHONE)
        self.find_element(LoginPageLocators.SEND_BUTTON_NEXT)

    @allure.step("Вводим номер телефона")
    def enter_phone(self, TEL):
        self.find_element(LoginPageLocators.INPUT_PHONE).send_keys(9085728301)
        self.attach_screenshot()


