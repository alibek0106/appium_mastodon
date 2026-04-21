def test_dynamic_feed_swipes(navigate_to_explore):
    explore_page = navigate_to_explore['explore_page']

    # Step 4: Scroll to the 4th post in the current live feed
    success = explore_page.scroll_to_post_by_index(4)
    assert success, "Could not find 4 posts in the feed"

    # Step 5: Swipe back to top
    explore_page.swipe_to_top_coordinates()

    # Step 6: Perform the 'Raw' swipe to the 20th post
    reached_20 = explore_page.swipe_to_20th_post_raw()
    assert reached_20, "Failed to iterate through 20 unique posts"

def test_context_investigation(navigate_to_explore):
    explore_page = navigate_to_explore['explore_page']

    # 4. Get the current context
    current = explore_page.get_current_context()
    print(f"\nInitial context: {current}")

    # 5. Check if there are other contexts
    all_contexts = explore_page.get_all_available_contexts()
    print(f"Available contexts: {all_contexts}")

    # 6. If those contexts are there, switch to them
    if len(all_contexts) > 1:
        switched = explore_page.switch_to_webview_if_available()
        if switched:
            explore_page.switch_to_native()
        else:
            print("No WebView found, staying in Native")
    else:
        print("Only NATIVE_APP context available")
