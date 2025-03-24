import pytest
from pages.auth_page import AuthPage
from pages.admin_license_page import AdminLicensePage
from config.config import ADMIN_LOGIN, ADMIN_PASSWORD

def test_admin_license_activation(page):
    auth_page = AuthPage(page)
    license_page = AdminLicensePage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)

    # Основные шаги
    license_page.navigate_to_accounts()
    license_page.search_user("andrey@mailforspam.com")
    license_page.select_user()
    license_page.activate_license()
    license_page.verify_success()