import pytest
from pages.auth_page import AuthPage
from pages.import_page import ImportPage
import config


def test_ad_import_with_filter(page, stand):
    auth_page = AuthPage(page)
    import_page = ImportPage(page)

    try:
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

        import_page.navigate_to_devices()
        import_page.open_import_modal()
        import_page.fill_connection_form()
        import_page.select_devices()
        import_page.perform_import()

        assert import_page.verify_result(), "Импорт не выполнен успешно"

    except Exception as e:
        pytest.fail(f"Ошибка на стенде {stand}: {str(e)}")
