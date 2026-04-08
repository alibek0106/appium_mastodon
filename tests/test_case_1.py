from pages.welcome_page import WelcomePage
from pages.server_login_page import ServerLoginPage
from pages.home_page import HomePage
from pages.explore_page import ExplorePage
from pages.post_details_page import PostDetailsPage
from data.config import Config
import time

def test_mastodon_flow(driver):
    APP_PACKAGE = Config.APP_PACKAGE
    
    welcome_page = WelcomePage(driver)
    login_page = ServerLoginPage(driver)
    home_page = HomePage(driver)
    explore_page = ExplorePage(driver)
    post_details_page = PostDetailsPage(driver)

    #1: Open Mastodon
    assert welcome_page.is_welcome_screen_displayed(), "Welcome screen not displayed!"

    # 2: Close mastodon without closing the session 
    welcome_page.terminate_mobile_app(APP_PACKAGE)
    time.sleep(2) # Brief pause for OS to kill process
    app_state = welcome_page.get_app_state(APP_PACKAGE)
    assert app_state == 1, f"App did not close! State is {app_state}"

    # 3: Open mastodon 
    welcome_page.activate_mobile_app(APP_PACKAGE)
    assert welcome_page.is_welcome_screen_displayed(), "Welcome screen not displayed after relaunch!"

    # 4: Log in to the app 
    welcome_page.click_log_in()
    login_page.enter_server_name(Config.SERVER_NAME)
    login_page.click_server()
    login_page.click_next()
    login_page.click_authorize()
    home_page.handle_notification_popup()
    assert home_page.is_home_screen_displayed(), "Home screen not displayed after login!"

    # 5: Tap 'Explore' tab 
    home_page.click_explore_tab()
    assert explore_page.is_explore_screen_displayed(), "Explore screen not displayed!"

    # 6: Open the first post 
    explore_page.click_first_post()
    assert post_details_page.is_post_displayed(), "Post details not opened!"

    # 7: Close the app and the session 
    print("Step 7: Handled automatically by the conftest.py teardown (yield)!")