from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
import allure

class PageMonitoringsExcludeLocators:
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
    ADD_EXCEPTION_BUTTON = (By.XPATH, '//*[@class="promo-add-rule add-exclude"]')
    CHANGE_HISTORY_LINK = (By.XPATH, '//*[@class="change-history"]')


class PageMonitoringsExclude(BasePage):

    def __init__(self, driver):

        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(PageMonitoringsExcludeLocators.INPUT_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.INPUT_CODE)
        self.find_element(PageMonitoringsExcludeLocators.SUBJECT_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.RELATION_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.COMPETITIR_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.PERIOD_FROM_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.PERIOD_TO_FIELD)
        self.find_element(PageMonitoringsExcludeLocators.SHOW_BUTTON)
        self.find_element(PageMonitoringsExcludeLocators.PRINT_BUTTON)
        self.find_element(PageMonitoringsExcludeLocators.EXCEL_BUTTON)
        self.find_element(PageMonitoringsExcludeLocators.TABLE_HEAD)
        self.find_element(PageMonitoringsExcludeLocators.ADD_EXCEPTION_BUTTON)
        self.find_element(PageMonitoringsExcludeLocators.CHANGE_HISTORY_LINK)


