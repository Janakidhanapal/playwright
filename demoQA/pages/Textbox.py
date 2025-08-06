from playwright.sync_api import Page

from faker import Faker

fake = Faker()

ELEMENTS_PAGE_HEADER_LOCATOR = 'div:has-text("Please select an item from left to start practice.")'
SIDE_PANEL_MENU_HEADER_ELEMENTS_LOCATOR = '.header-text:has-text("Elements")'
SIDE_PANEL_MENU_ITEM_TEXTBOX_LOCATOR = 'span:has-text("Text Box")'
FULL_NAME_INPUT_LOCATOR = '#userName'
EMAIL_INPUT_LOCATOR = '#userEmail'
CURRENT_ADDRESS_INPUT_LOCATOR = '#currentAddress'
PERMANENT_ADDRESS_INPUT_LOCATOR = '#permanentAddress'


def verify_elements_page_loaded(page: Page):
    page.wait_for_selector(ELEMENTS_PAGE_HEADER_LOCATOR, timeout=10_000, state="visible")


def click_side_panel_menu_item_textbox(page: Page):
    (page
     .locator('.element-group', has=page.locator(SIDE_PANEL_MENU_HEADER_ELEMENTS_LOCATOR))
     .locator(SIDE_PANEL_MENU_ITEM_TEXTBOX_LOCATOR).click())


def fill_submit_textbox(page: Page, full_name='', email='', current_address='', permanent_address=''):
    page.locator(FULL_NAME_INPUT_LOCATOR).fill(full_name if full_name != '' else fake.name())
    page.locator(EMAIL_INPUT_LOCATOR).fill(email if email != '' else fake.email())
    page.locator(CURRENT_ADDRESS_INPUT_LOCATOR).fill(current_address if current_address != '' else fake.address())
    page.locator(PERMANENT_ADDRESS_INPUT_LOCATOR).fill(permanent_address if permanent_address != '' else fake.address())
    page.locator('#submit').click()