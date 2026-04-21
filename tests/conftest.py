import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from data.config import Config
from pages.welcome_page import WelcomePage
from pages.server_login_page import ServerLoginPage
from pages.home_page import HomePage
from pages.explore_page import ExplorePage

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

@pytest.fixture
def navigate_to_explore(driver):
    # Precondition Fixture: Logs in and navigates to the Explore tab
    welcome_page = WelcomePage(driver)
    login_page = ServerLoginPage(driver)
    home_page = HomePage(driver)
    explore_page = ExplorePage(driver)

    welcome_page.click_log_in()
    login_page.enter_server_name(Config.SERVER_NAME)
    login_page.click_server()
    login_page.click_next()
    login_page.click_authorize()
    
    home_page.handle_notification_popup()
    home_page.click_explore_tab()

    assert explore_page.is_explore_screen_displayed(), "[PRECONDITION FAILED] Explore screen did not load!"
        
    # Return the page objects
    return {
        'driver': driver,
        'explore_page': explore_page
    }