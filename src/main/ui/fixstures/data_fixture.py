import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture(scope="session")
def playwright_insance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_insance):
    browser = playwright_insance.chromium.launch(headless=False, slow_mo=500)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()



