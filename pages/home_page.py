from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    HOME_SCREEN_INDICATOR = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Home"])[1]')
    EXPLORE_TAB = (AppiumBy.ACCESSIBILITY_ID, 'Search')

    def is_home_screen_displayed(self):
        return self.is_displayed(self.HOME_SCREEN_INDICATOR)
    
    def click_explore_tab(self):
        self.click_element(self.EXPLORE_TAB)