from playwright.sync_api import Page

ELEMENTS_LOCATOR = 'h5:has-text("Elements")'


def click_elements(page: Page):
    page.locator(ELEMENTS_LOCATOR).click()
