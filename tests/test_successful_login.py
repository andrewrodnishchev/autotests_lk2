import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage

@pytest.mark.smoke
def test_successful_login(page):
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)

    auth_page.should_be_on_dashboard()
    auth_page.should_see_welcome_message()