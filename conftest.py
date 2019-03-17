import sys
import main
import pytest
from selenium import webdriver
from configuration.config import Config

config = Config()
fixture_scope = "class"


@pytest.fixture(scope=fixture_scope)
def one_time_setup(request, get_driver):
    # This is setUp fixture that will run before each test
    base_url = config.base_url
    credentials = config.credentials
    if request.cls is not None:
        request.cls.driver = driver
        request.cls.base_url = base_url
        request.cls.credentials = credentials
    driver.maximize_window()
    yield driver, base_url, credentials

    # This will tearDown the browser after each test
    driver.quit()


@pytest.fixture(scope=fixture_scope)
def get_driver():
    # This fixture will initialize browser depending on browser selection in User_settings.py and Operating System
    os_platform = sys.platform
    webdriver_path = main.base_directory + '/webdrivers/'
    global driver
    if os_platform == "darwin":  # Mac OS
        if config.browser.upper() == str("chrome").upper():
            driver = webdriver.Chrome(executable_path=webdriver_path + 'chromedriver')
        if config.browser.upper() == str("firefox").upper():
            driver = webdriver.Firefox(executable_path=webdriver_path + 'geckodriver')
        if config.browser.upper() == str("Safari").upper():
            driver = webdriver.Safari()
    elif os_platform == "win32":  # Windows OS
        if config.browser.upper() == str("chrome").upper():
            driver = webdriver.Chrome(executable_path=webdriver_path + 'chromedriver.exe')
        if config.browser.upper() == str("firefox").upper():
            driver = webdriver.Firefox(executable_path=webdriver_path + 'geckodriver.exe')
        if config.browser.upper() == str("safari").upper():
            raise Exception("This OS doesn't support Safari Browser!")
    return driver
