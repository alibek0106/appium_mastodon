from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 

class HomePage(BasePage):
    HOME_SCREEN_INDICATOR = (AppiumBy.XPATH, '(//android.widget.TextView[@text="Home"])[1]')
    EXPLORE_TAB = (AppiumBy.ACCESSIBILITY_ID, 'Search')
    ALLOW_NOTIFICATIONS_BTN = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')

    def is_home_screen_displayed(self):
        return self.is_displayed(self.HOME_SCREEN_INDICATOR)
    
    def click_explore_tab(self):
        self.click_element(self.EXPLORE_TAB)

    def handle_notification_popup(self):
        try:
            short_wait = WebDriverWait(self.driver, 4)
            allow_btn = short_wait.until(EC.element_to_be_clickable(self.ALLOW_NOTIFICATIONS_BTN))
            allow_btn.click()
        except TimeoutException:
            print('No pop-up appeared')