import pytest
from pages.auth_page import AuthPage
import config


@pytest.mark.regression
def test_unsuccessful_login(page, stand):
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.INCORRECT_PASSWORD)
    auth_page.should_see_error_message()
