# conftest.py
import pytest
from playwright.sync_api import sync_playwright
import config


def pytest_addoption(parser):
    parser.addoption(
        "--stand",
        action="store",
        default=config.SELECTED_STAND,
        help=f"Set test stand: {', '.join(config.STANDS.keys())}"
    )


@pytest.fixture(scope="session")
def stand(request):
    return request.config.getoption("--stand")


@pytest.fixture(scope="session", autouse=True)
def setup_stand(stand):
    if stand not in config.STANDS:
        raise ValueError(f"Invalid stand: {stand}")
    config.SELECTED_STAND = stand


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,  # True - для Git, False - локально
            args=["--start-maximized"]
        )
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
    page.evaluate("document.querySelectorAll('.modal').forEach(m => m.remove())")
