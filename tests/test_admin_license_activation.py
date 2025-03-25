import pytest
from pages.auth_page import AuthPage
from pages.admin_license_page import AdminLicensePage
import config


def test_admin_license_activation(page, stand):
    auth_page = AuthPage(page)
    license_page = AdminLicensePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    license_page.navigate_to_accounts()
    license_page.search_user("andrey@mailforspam.com")
    license_page.select_user()
    license_page.activate_license()
    license_page.verify_success()
