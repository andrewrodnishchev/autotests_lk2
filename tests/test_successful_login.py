import pytest
from pages.auth_page import AuthPage
import config


@pytest.mark.smoke
def test_successful_login(page, stand):
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    auth_page.should_be_on_dashboard()
