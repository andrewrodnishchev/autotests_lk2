import pytest
from pages.auth_page import AuthPage
from pages.device_license_page import DeviceLicensePage
import config


def test_device_license_activation(page, stand):
    auth_page = AuthPage(page)
    license_page = DeviceLicensePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    license_page.navigate_to_devices()
    license_page.search_device("135 026 892")
    license_page.select_device()
    license_page.activate_license()
    license_page.verify_success()
