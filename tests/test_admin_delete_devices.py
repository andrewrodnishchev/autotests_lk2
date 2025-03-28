import pytest
from pages.auth_page import AuthPage
from pages.admin_delete_devices_page import AdminDeleteDevicesPage
import config


def test_admin_delete_devices(page, stand):
    auth_page = AuthPage(page)
    admin_page = AdminDeleteDevicesPage(page)
    TEST_DEVICE_ID = "076 897 034"

    try:
        # Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

        # Основные шаги
        admin_page.navigate_to_devices_section()
        admin_page.search_device(TEST_DEVICE_ID)
        admin_page.select_device()
        admin_page.delete_device()
        admin_page.verify_deletion_success()

    except Exception as e:
        page.screenshot(path=f"admin_delete_error_{stand}.png")
        pytest.fail(f"Ошибка удаления устройства на стенде {stand}: {str(e)}")
