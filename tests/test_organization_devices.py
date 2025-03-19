# tests/test_organization_devices.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.organization_devices_page import OrganizationDevicesPage

@pytest.mark.regression
def test_add_device_to_organization(page):
    auth_page = AuthPage(page)
    org_devices_page = OrganizationDevicesPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств организации
    org_devices_page.navigate_to_organization_devices()

    # Добавление устройства
    org_devices_page.add_device("135026892")

    # Проверка уведомления об успешном добавлении
    org_devices_page.should_see_success_add_message()