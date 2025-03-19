# tests/test_bulk_edit.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.bulk_edit_page import BulkEditPage

@pytest.mark.regression
def test_bulk_edit_devices(page):
    auth_page = AuthPage(page)
    bulk_edit_page = BulkEditPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств
    bulk_edit_page.navigate_to_organization_devices()

    # Выбор чекбокса
    bulk_edit_page.select_device_checkbox()

    # Открытие меню редактирования
    bulk_edit_page.open_edit_menu()

    # Выбор политики инвентаризации
    bulk_edit_page.select_inventory_policy()

    # Выполнение изменений
    bulk_edit_page.execute_changes()

    # Проверка уведомления
    bulk_edit_page.should_see_success_message()