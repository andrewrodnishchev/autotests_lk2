# tests/test_activate_license.py
import pytest
from pages.auth_page import AuthPage
from pages.license_page import LicensePage
import config


@pytest.mark.regression
def test_activate_license(page, stand):
    auth_page = AuthPage(page)
    license_page = LicensePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    license_page.navigate_to_organization_devices()
    license_page.select_device_checkbox()
    license_page.activate_license()
    license_page.confirm_activation()
    license_page.should_see_success_message()
