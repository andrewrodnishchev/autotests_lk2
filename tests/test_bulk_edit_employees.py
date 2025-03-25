# tests/test_bulk_edit_employees.py

import pytest
from pages.auth_page import AuthPage
from pages.employee_page import EmployeePage
import config


@pytest.mark.regression
def test_bulk_edit_employees(page, stand):
    auth_page = AuthPage(page)
    employee_page = EmployeePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    employee_page.navigate_to_organization_employees()
    employee_page.select_all_employees()
    employee_page.open_edit_menu()
    employee_page.set_no_change_option()
    employee_page.execute_changes()
    employee_page.should_see_success_message()
