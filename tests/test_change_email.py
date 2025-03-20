import pytest
from pages.admin_page import AdminPage
from pages.auth_page import AuthPage
from config.config import ADMIN_LOGIN, ADMIN_PASSWORD

def test_change_email(page):
    auth_page = AuthPage(page)
    admin_page = AdminPage(page)

    # Авторизация администратора
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)

    # Переход в администрирование
    admin_page.navigate_to_administration()
    admin_page.open_accounts()

    # Поиск пользователя
    admin_page.search_user("rodnischev@safib.ru")

    # Редактирование почты
    admin_page.open_edit_menu()
    admin_page.update_email("rodnischev@safib.ru")
    admin_page.save_changes()

    # Проверка успеха
    admin_page.verify_success()