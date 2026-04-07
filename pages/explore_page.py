from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ExplorePage(BasePage):
    EXPLORE_SCREEN_INDICATOR = (AppiumBy.ID, 'org.joinmastodon.android:id/discover_content')
    FIRST_POST_ITEM = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.joinmastodon.android:id/text"]')

    def is_explore_screen_displayed(self):
        return self.is_displayed(self.EXPLORE_SCREEN_INDICATOR)
    
    def click_first_post(self):
        self.click_element(self.FIRST_POST_ITEM)