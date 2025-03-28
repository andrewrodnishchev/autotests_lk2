# tests/test_admin_add_devices.py
import pytest
from pages.auth_page import AuthPage
from pages.admin_devices_page import AdminDevicesPage
import config


def test_admin_add_devices(page, stand):
    auth_page = AuthPage(page)
    admin_page = AdminDevicesPage(page)
    TEST_DEVICE_ID = "076 897 034"

    try:
        # Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

        # Основные шаги
        admin_page.navigate_to_devices_section()
        admin_page.search_device(TEST_DEVICE_ID)
        admin_page.select_device()
        admin_page.add_to_organization()
        admin_page.verify_success()

    except Exception as e:
        page.screenshot(path=f"admin_add_devices_error_{stand}.png")
        pytest.fail(f"Ошибка добавления устройств на стенде {stand}: {str(e)}")
