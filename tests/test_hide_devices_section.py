# tests/test_hide_devices_section.py
import pytest
from pages.auth_page import AuthPage
from pages.license_activation_page import LicenseActivationPage
import config


def test_devices_section_hidden_after_license_activation(page):
    auth_page = AuthPage(page)
    license_page = LicenseActivationPage(page)

    try:
        # Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

        # Основные шаги
        license_page.go_to_admin_section()
        license_page.search_account(config.LOGIN)  # Добавлен поиск аккаунта
        license_page.open_account_actions_menu()
        license_page.activate_license_with_restriction()

        # Проверка скрытия раздела
        license_page.open_my_assistant()
        license_page.verify_devices_section_hidden()

    except Exception as e:
        pytest.fail(f"Ошибка проверки скрытия раздела: {str(e)}")
