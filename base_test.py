import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--allow-profiles-outside-user-dir')
    # options.add_argument('--enable-profile-shortcut-manager')
    options.add_argument(f'--user-data-dir=./user_data')
    options.add_argument('--profile-directory=Profile_1')
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
