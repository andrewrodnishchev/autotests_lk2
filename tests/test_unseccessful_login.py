import pytest
from config.config import LOGIN, INCORRECT_PASSWORD
from pages.auth_page import AuthPage

@pytest.mark.regression
def test_unsuccessful_login(page):
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, INCORRECT_PASSWORD)

    auth_page.should_see_error_message()