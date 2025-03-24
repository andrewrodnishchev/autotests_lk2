import pytest
from pages.auth_page import AuthPage
from pages.device_license_page import DeviceLicensePage
from config.config import ADMIN_LOGIN, ADMIN_PASSWORD

def test_device_license_activation(page):
    auth_page = AuthPage(page)
    license_page = DeviceLicensePage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)

    # Основные шаги
    license_page.navigate_to_devices()
    license_page.search_device("135 026 892")
    license_page.select_device()
    license_page.activate_license()
    license_page.verify_success()