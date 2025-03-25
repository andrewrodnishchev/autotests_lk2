import pytest
from pages.auth_page import AuthPage
from pages.import_ou_page import ImportOUPage
import config


def test_ou_import(page, stand):
    auth_page = AuthPage(page)
    import_page = ImportOUPage(page)

    try:
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
        import_page.navigate_to_devices()
        import_page.open_import_modal()
        import_page.fill_connection_details()
        import_page.search_and_select_device()
        import_page.perform_import()
        assert import_page.verify_success(), "Импорт OU не выполнен успешно"
    except Exception as e:
        page.screenshot(path=f"ou_import_error_{stand}.png")
        pytest.fail(f"Ошибка на стенде {stand}: {str(e)}")
