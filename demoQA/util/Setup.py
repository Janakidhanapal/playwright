from playwright.sync_api import Playwright, Page
import os
from datetime import datetime


def set_browser(playwright: Playwright):
    # Channel can be "chrome", "msedge", "chrome-beta", "msedge-beta" or "msedge-dev".
    browser_type = playwright.chromium.launch(channel="msedge", headless=False)
    page = browser_type.new_page()
    return page


def take_screenshot(page: Page, name="screenshot"):
    path = get_unique_file_name('screenshots', 'screenshot')
    os.makedirs("screenshots", exist_ok=True)
    page.screenshot(path=path)


def get_unique_file_name(dir_name, file_prefix):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(dir_name, f"{file_prefix}_{timestamp}.png")
