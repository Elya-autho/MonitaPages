from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure


class ExceptionPageLocators:
    INPUT_FIELD = (By.XPATH, '//*[@class="st-filter-input st-filter-name"]')
    INPUT_CODE = (By.XPATH, '//*[@class="st-filter-input st-filter-code"]')
    SUBJECT_FIELD = (By.XPATH, '//*[@class="mon-filter-span mon-filter-region"]')
    RELATION_FIELD = (By.XPATH, '//*[@class="mon-filter-span mon-filter-relation"]')
    COMPETITIR_FIELD = (By.XPATH, '//*[@class="mon-filter-span mon-filter-network"]')
    PERIOD_FROM_FIELD = (By.XPATH, '//*[@class="mon-filter-period-input mon-filter-period-from "]')
    PERIOD_TO_FIELD = (By.XPATH, '//*[@class="mon-filter-period-input mon-filter-period-to"]')
    CLEAN_BUTTON = (By.XPATH, '//*[@class="button button--blue mon-filter-clean"]')
    SHOW_BUTTON = (By.XPATH, '//*[@class="button button--lightGreen mon-filter-show"]')
    PRINT_BUTTON = (By.XPATH, '//*[@class="button button__print button--grey mon-print"]')
    EXCEL_BUTTON = (By.XPATH, '//*[@class="button button_document button--green mon-excel"]')
    TABLE_HEAD = (By.XPATH, '// *[@class ="table-head-tr border-none"]')
    ADD_EXCEPTION_BUTTON =(By.XPATH, '//*[@class="promo-add-rule add-exclude"]')
    CHANGE_HISTORY_LINK = (By.XPATH, '//*[@class="change-history"]')
    INPUT_PHONE = (By.CLASS_NAME,'login-phone-number')
    SEND_BUTTON_NEXT = (By.XPATH, '//*[@class="login-phone-next"]')
class ExceptionPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(ExceptionPageLocators.INPUT_FIELD)
        self.find_element(ExceptionPageLocators.INPUT_CODE)
        self.find_element(ExceptionPageLocators.SUBJECT_FIELD)
        self.find_element(ExceptionPageLocators.RELATION_FIELD)
        self.find_element(ExceptionPageLocators.COMPETITIR_FIELD)
        self.find_element(ExceptionPageLocators.PERIOD_FROM_FIELD)
        self.find_element(ExceptionPageLocators.PERIOD_TO_FIELD)
        self.find_element(ExceptionPageLocators.SHOW_BUTTON)
        self.find_element(ExceptionPageLocators.PRINT_BUTTON)
        self.find_element(ExceptionPageLocators.EXCEL_BUTTON)
        self.find_element(ExceptionPageLocators.TABLE_HEAD)
        self.find_element(ExceptionPageLocators.ADD_EXCEPTION_BUTTON)
        self.find_element(ExceptionPageLocators.CHANGE_HISTORY_LINK)
        self.find_element(ExceptionPageLocators.INPUT_PHONE)
        self.find_element(ExceptionPageLocators.SEND_BUTTON_NEXT)


