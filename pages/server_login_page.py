from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class ServerLoginPage(BasePage):
    NEXT_BUTTON = (AppiumBy.ID, 'org.joinmastodon.android:id/btn_next')
    AUTHORIZE_BUTTON = (AppiumBy.XPATH, '//android.widget.Button[@text="Authorize"]')
    SERVER_INPUT_FIELD = (AppiumBy.ID, 'org.joinmastodon.android:id/search_edit')
    SERVER_BUTTON = (AppiumBy.ID, 'org.joinmastodon.android:id/radiobtn')

    def enter_server_name(self, server_url):
        self.input_text(self.SERVER_INPUT_FIELD, server_url)

    def click_server(self):
        self.click_element(self.SERVER_BUTTON)

    def click_next(self):
        self.click_element(self.NEXT_BUTTON)

    def click_authorize(self):
        self.click_element(self.AUTHORIZE_BUTTON)