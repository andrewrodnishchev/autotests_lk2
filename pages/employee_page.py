# pages/employee_page.py
import time

from playwright.sync_api import Page, expect
from locators.employee_locators import EmployeeLocators

class EmployeePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_organization_employees(self):
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(EmployeeLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Сотрудники'")
        self.page.click(EmployeeLocators.EMPLOYEES_MENU)

    def select_all_employees(self):
        print("Выбор всех сотрудников")
        checkbox = self.page.locator(EmployeeLocators.SELECT_ALL_CHECKBOX)
        checkbox.wait_for(state="visible", timeout=10000)
        time.sleep(1)
        checkbox.click()  # Явный клик по чекбоксу
        print("Чекбокс выбран")

    def open_edit_menu(self):
        print("Нажатие на кнопку 'Изменить'")
        self.page.click(EmployeeLocators.EDIT_BUTTON)

    def set_no_change_option(self):
        print("Выбор опции 'Не изменять'")
        self.page.click(EmployeeLocators.LIST_DROPDOWN)
        option = self.page.locator(EmployeeLocators.NO_CHANGE_OPTION)
        option.wait_for(state="visible", timeout=10000)
        option.click()

    def execute_changes(self):
        print("Нажатие на кнопку 'Выполнить'")
        self.page.click(EmployeeLocators.EXECUTE_BUTTON)
        self.page.wait_for_timeout(2000)  # Ожидание загрузки

    def should_see_success_message(self):
        print("Проверка уведомления об успешном изменении")
        success_msg = self.page.locator(EmployeeLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()