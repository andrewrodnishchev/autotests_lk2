import pytest
from pages.auth_page import AuthPage
from pages.import_page import ImportPage
from config.config import LOGIN, CORRECT_PASSWORD

def test_ad_import_with_filter(page):
    auth_page = AuthPage(page)
    import_page = ImportPage(page)

    try:
        # Авторизация
        page.goto("http://lk.corp.dev.ru/Account/Login")
        auth_page.login(LOGIN, CORRECT_PASSWORD)

        # Основные шаги
        import_page.navigate_to_devices()
        import_page.open_import_modal()
        import_page.fill_connection_form()
        import_page.select_devices()
        import_page.perform_import()
        import_page.verify_result()

    except Exception as e:
        page.screenshot(path="import_error.png")
        pytest.fail(f"Ошибка выполнения теста: {str(e)}")