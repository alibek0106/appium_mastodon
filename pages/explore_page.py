from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

class ExplorePage(BasePage):
    EXPLORE_SCREEN_INDICATOR = (AppiumBy.ID, 'org.joinmastodon.android:id/discover_content')
    FIRST_POST_ITEM = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="org.joinmastodon.android:id/text"]')
    SEARCH_INPUT_BTN = (AppiumBy.ID, 'org.joinmastodon.android:id/search_text')
    SEARCH_INPUT_FIELD = (AppiumBy.CLASS_NAME, 'android.widget.EditText')

    def is_explore_screen_displayed(self):
        return self.is_displayed(self.EXPLORE_SCREEN_INDICATOR)
    
    def click_first_post(self):
        self.click_element(self.FIRST_POST_ITEM)

    def are_posts_displayed(self):
        return self.is_displayed(self.FIRST_POST_ITEM)
    
    def get_search_field_position(self):
        return self.get_element_location(self.SEARCH_INPUT_BTN)
    
    def enter_search_query(self, text):
        self.click_element(self.SEARCH_INPUT_BTN)
        self.input_text(self.SEARCH_INPUT_FIELD, text)

    def clear_search_field(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SEARCH_INPUT_FIELD))
        element.clear()

    def get_search_field_text(self):
        return self.get_element_text(self.SEARCH_INPUT_FIELD)
    
    def click_search_btn(self):
        self.click_element(self.SEARCH_INPUT_BTN)

    def click_search_field(self):
        self.click_element(self.SEARCH_INPUT_FIELD)

    def send_enter_via_sendkeys(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT_FIELD))
        element.send_keys('\n')