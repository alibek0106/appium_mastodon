import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from data.config import Config

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = Config.APP_PACKAGE
    options.app_activity = Config.APP_ACTIVITY
    options.no_reset = True  

    driver = webdriver.Remote(Config.APPIUM_SERVER, options=options)
    
    yield driver

    driver.execute_script('mobile: clearApp', {'appId': Config.APP_PACKAGE})
    
    driver.quit()