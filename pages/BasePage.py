from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_test import browser
from pages.ExceptionPage import ExceptionPageHelper
import allure

BASE_URL ="https://test.kb-monita.ru/#monitorings_exclude"




class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(expected_conditions.visibility_of_element_located(locator),message=f"Не удалось найти элемент{locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver,time).until(expected_conditions.visibility_of_all_elements_located(locator),message=f"Не удалось найти элементы{locator}")

    @allure.step("Открываем страницу")
    def get_url(self,url):
        return self.driver.get(url)

    def auth(self, tel):
        driver = self.driver
        input_auth = driver.find_element(ExceptionPageHelper.INPUT_PHONEPUT_PHONE)
        input_auth.send_keys(tel)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(),"скриншот", allure.attachment_type.PNG)



