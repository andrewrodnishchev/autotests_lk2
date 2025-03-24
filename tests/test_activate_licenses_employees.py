# tests/test_activate_licenses.py

import pytest
from pages.auth_page import AuthPage
from pages.activate_license_page import LicensePage
from config.config import LOGIN, CORRECT_PASSWORD  # Используем админские данные!

def test_activate_licenses(page):
    auth_page = AuthPage(page)
    license_page = LicensePage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(LOGIN, CORRECT_PASSWORD)  # Используем админский логин!

    # Основные шаги
    license_page.navigate_to_employee_section()
    license_page.select_employee()
    license_page.open_edit_menu()
    license_page.select_license()
    license_page.execute_changes()
    license_page.verify_success()