import pytest
from pages.auth_page import AuthPage
from pages.admin_accounts_page import AdminAccountsPage
from config.config import ADMIN_LOGIN, ADMIN_PASSWORD

def test_add_user_to_organization(page):
    auth_page = AuthPage(page)
    admin_page = AdminAccountsPage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)

    # Основные шаги
    admin_page.navigate_to_accounts()
    admin_page.search_user("andrey@mailforspam.com")
    admin_page.select_user()
    admin_page.open_add_to_org_modal()
    admin_page.select_organization()
    admin_page.toggle_checkbox()
    admin_page.execute_action()
    admin_page.verify_error()