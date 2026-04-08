from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def is_displayed(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
        
    def get_element_location(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.location
    
    def get_element_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
            
    def get_app_state(self, package_name):
        return self.driver.query_app_state(package_name)
    
    def terminate_mobile_app(self, package_name):
        self.driver.terminate_app(package_name)

    def activate_mobile_app(self, package_name):
        self.driver.activate_app(package_name)