import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.close()

@pytest.fixture(autouse=True)
def close_modals(page):
    yield
    # Закрываем все модальные окна после теста
    page.evaluate("document.querySelectorAll('.modal').forEach(m => m.remove())")