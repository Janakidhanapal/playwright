from playwright.sync_api import sync_playwright

from demoQA.pages import Home, Textbox
from demoQA.util import Setup, TearDown

with sync_playwright() as playwright:
    page = Setup.set_browser(playwright)
    page.goto('https://demoqa.com/')
    Home.click_elements(page)
    Textbox.verify_elements_page_loaded(page)
    Textbox.click_side_panel_menu_item_textbox(page)
    Textbox.fill_submit_textbox(page)
    page.wait_for_timeout(5000)
    Setup.take_screenshot(page)
    TearDown.close_browser(page)
