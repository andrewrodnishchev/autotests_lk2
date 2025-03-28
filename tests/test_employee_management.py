# tests/test_employee_management.py
import pytest
from pages.auth_page import AuthPage
from pages.employee_management_page import EmployeeManagementPage
import config


def test_employee_management(page, stand):
    auth_page = AuthPage(page)
    employee_page = EmployeeManagementPage(page)
    TEST_EMAIL = "ast1@mailforspam.com"

    try:
        # 1. Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

        # 2. Переход в организацию
        employee_page.navigate_to_organization()

        # 3. Открытие раздела сотрудников
        employee_page.open_employees_section()

        # 4. Добавление нового сотрудника
        employee_page.add_new_employee(TEST_EMAIL)

        # 5. Проверка успешного добавления
        employee_page.verify_add_success()

        # 6. Поиск и удаление сотрудника
        employee_page.search_and_delete_employee(TEST_EMAIL)

        # 7. Проверка успешного удаления
        employee_page.verify_delete_success()

    except Exception as e:
        page.screenshot(path=f"screenshots/employee_management_error_{stand}.png")
        pytest.fail(f"Ошибка управления сотрудниками на стенде {stand}: {str(e)}")
