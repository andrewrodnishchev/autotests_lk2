# tests/test_activate_licenses.py
import pytest
from pages.auth_page import AuthPage
from pages.activate_license_page import LicensePage
import config


def test_activate_licenses(page, stand):
    auth_page = AuthPage(page)
    license_page = LicensePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

    license_page.navigate_to_employee_section()
    license_page.select_employee()
    license_page.open_edit_menu()
    license_page.select_license()
    license_page.execute_changes()
    license_page.verify_success()
