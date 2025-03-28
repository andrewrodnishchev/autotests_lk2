import pytest
from pages.auth_page import AuthPage
from pages.device_import_page import DeviceImportPage
import config


def test_ad_device_import(page, stand):
    auth_page = AuthPage(page)
    import_page = DeviceImportPage(page)

    # Тестовые данные
    TEST_SERVER = "smbdomain.dom:636:s"
    TEST_USER = "test_user"
    TEST_PASSWORD = "Zxcv432!"

    try:
        # Авторизация под админом
        auth_page.navigate_to_login_page()
        auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

        # Основные шаги теста
        import_page.navigate_to_organization()
        import_page.open_devices_section()
        import_page.start_ad_import()
        import_page.fill_connection_details(TEST_SERVER, TEST_USER, TEST_PASSWORD)
        import_page.submit_import()
        import_page.apply_registration_filter()

        # Проверка результата
        import_page.verify_domain_present()

    except Exception as e:
        page.screenshot(path=f"ad_import_error_{stand}.png")
        pytest.fail(f"Ошибка импорта устройств на стенде {stand}: {str(e)}")
