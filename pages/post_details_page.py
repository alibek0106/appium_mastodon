from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class PostDetailsPage(BasePage):
    POST_DETAILS_INDICATOR = (AppiumBy.ID, 'org.joinmastodon.android:id/text')

    def is_post_displayed(self):
        return self.is_displayed(self.POST_DETAILS_INDICATOR)