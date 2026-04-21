from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import time

class ExplorePage(BasePage):
    EXPLORE_SCREEN_INDICATOR = (AppiumBy.ID, 'org.joinmastodon.android:id/discover_content')
    POST_TEXT_BODY = (AppiumBy.ID, 'org.joinmastodon.android:id/text')

    def is_explore_screen_displayed(self):
        return self.is_displayed(self.EXPLORE_SCREEN_INDICATOR)
    
    def click_first_post(self):
        self.click_element(self.FIRST_POST_ITEM)

    def get_visible_post_count(self):
        return len(self.driver.find_elements(*self.POST_TEXT_BODY))
    
    def scroll_to_post_by_index(self, target_index):
        seen_posts = set()
        max_scrolls = 10
        
        window = self.driver.get_window_size()
        x = window['width'] // 2
        start_y = int(window['height'] * 0.8)
        end_y = int(window['height'] * 0.3)

        for _ in range(max_scrolls):
            elements = self.driver.find_elements(*self.POST_TEXT_BODY)
            
            for el in elements:
                identifier = el.text or el.get_attribute("content-desc")
                
                if identifier:
                    seen_posts.add(identifier)
                
                if len(seen_posts) >= target_index:
                    return True
            
            self.driver.swipe(x, start_y, x, end_y, 500)
            
        return False
    
    def swipe_to_top_coordinates(self):
        window = self.driver.get_window_size()
        x = window['width'] // 2
        start_y = int(window['height'] * 0.3)
        end_y = int(window['height'] * 0.8)
        
        for _ in range(3):
            self.driver.swipe(x, start_y, x, end_y, 600)

    def swipe_to_20th_post_raw(self):
        found_posts = set()
        target = 20
        
        window = self.driver.get_window_size()
        x = window['width'] // 2
        start_y = int(window['height'] * 0.8)
        end_y = int(window['height'] * 0.3)
        
        while len(found_posts) < target:
            elements = self.driver.find_elements(*self.POST_TEXT_BODY)
            
            for el in elements:
                identifier = el.get_attribute("text") or el.get_attribute("content-desc")
                if identifier:
                    found_posts.add(identifier)
                
                if len(found_posts) >= target:
                    return True
            
            self.driver.swipe(x, start_y, x, end_y, 500)
            time.sleep(1) # Wait for network/lazy loading
            
        return False
    
    def get_current_context(self):
        return self.driver.context
    
    def get_all_available_contexts(self):
        return self.driver.contexts
    
    def switch_to_webview_if_available(self):
        contexts = self.get_all_available_contexts()
        for context in contexts:
            if "WEBVIEW" in context:
                self.driver.switch_to.context(context)
                return True
            return False
        
    def switch_to_native(self):
        self.driver.switch_to.context("NATIVE_APP")