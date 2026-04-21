from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class WelcomePage(BasePage):
    WELCOME_LOGO = (AppiumBy.ID, 'android:id/content')
    LOG_IN_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@resource-id="org.joinmastodon.android:id/btn_log_in"]')

    def is_welcome_screen_displayed(self):
        return self.is_displayed(self.WELCOME_LOGO)
    
    def click_log_in(self):
        self.click_element(self.LOG_IN_BUTTON)