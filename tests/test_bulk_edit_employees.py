# tests/test_bulk_edit_employees.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.employee_page import EmployeePage

@pytest.mark.regression
def test_bulk_edit_employees(page):
    auth_page = AuthPage(page)
    employee_page = EmployeePage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел сотрудников
    employee_page.navigate_to_organization_employees()

    # Выбор всех сотрудников
    employee_page.select_all_employees()

    # Открытие меню редактирования
    employee_page.open_edit_menu()

    # Выбор опции "Не изменять"
    employee_page.set_no_change_option()

    # Выполнение изменений
    employee_page.execute_changes()

    # Проверка уведомления
    employee_page.should_see_success_message()