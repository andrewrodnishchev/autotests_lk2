import pytest
from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage
import config


@pytest.mark.regression
def test_password_change(page, stand):
    auth_page = AuthPage(page)
    profile_page = ProfilePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    profile_page.open_profile_menu()
    profile_page.navigate_to_profile()
    profile_page.open_security_tab()
    profile_page.open_password_change_form()
    profile_page.change_password(
        old_pass=config.CORRECT_PASSWORD,
        new_pass=config.CORRECT_PASSWORD
    )
    profile_page.should_see_success_message()
