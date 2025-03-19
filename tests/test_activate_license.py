# tests/test_activate_license.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.license_page import LicensePage

@pytest.mark.regression
def test_activate_license(page):
    auth_page = AuthPage(page)
    license_page = LicensePage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств организации
    license_page.navigate_to_organization_devices()

    # Выбор чекбокса устройства
    license_page.select_device_checkbox()

    # Активация лицензии
    license_page.activate_license()

    license_page.confirm_activation()

    # Проверка уведомления
    license_page.should_see_success_message()