# pages/employee_management_page.py
from playwright.sync_api import Page, expect
from locators.employee_management_locators import EmployeeManagementLocators
import config
import time
import re


class EmployeeManagementPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_organization(self):
        try:
            self.page.wait_for_selector(
                EmployeeManagementLocators.ORGANIZATION_LINK,
                state="visible",
                timeout=config.DEFAULT_TIMEOUT * 2
            ).click()
            self.page.wait_for_load_state("networkidle")
        except Exception as e:
            raise

    def open_employees_section(self):
        try:
            self.page.wait_for_selector(
                EmployeeManagementLocators.EMPLOYEES_SECTION,
                state="visible",
                timeout=config.DEFAULT_TIMEOUT * 2
            ).click()
            self.page.wait_for_selector(
                EmployeeManagementLocators.ADD_EMPLOYEE_BUTTON,
                state="visible",
                timeout=config.DEFAULT_TIMEOUT * 3
            )
        except Exception as e:
            raise

    def add_new_employee(self, email: str):
        try:
            # Клик по кнопке добавления
            add_button = self.page.locator(EmployeeManagementLocators.ADD_EMPLOYEE_BUTTON)
            add_button.wait_for(state="visible")
            add_button.click()

            # Заполнение email
            email_field = self.page.locator(EmployeeManagementLocators.EMAIL_INPUT)
            email_field.wait_for(state="visible")
            email_field.fill(email)

            # Сохранение
            save_button = self.page.locator(EmployeeManagementLocators.SAVE_BUTTON)
            save_button.wait_for(state="visible")
            save_button.click()

            # Ожидание завершения операции
            self.page.wait_for_load_state("networkidle")
            time.sleep(1)  # Небольшая пауза

        except Exception as e:
            raise

    def verify_add_success(self):
        try:
            # Проверяем URL
            expect(self.page).to_have_url(re.compile(r".*Employers.*"), timeout=config.DEFAULT_TIMEOUT * 3)

            # Проверяем уведомление (если есть)
            if self.page.locator(EmployeeManagementLocators.SUCCESS_NOTIFICATION).count() > 0:
                notification = self.page.locator(EmployeeManagementLocators.SUCCESS_NOTIFICATION)
                notification.wait_for(state="visible")
                expect(notification).to_contain_text("Приглашение сотрудника в организацию успешно создано")

            time.sleep(1)  # Пауза для визуальной проверки

        except Exception as e:
            raise

    def search_and_delete_employee(self, email: str):
        try:
            # Поиск сотрудника
            search_field = self.page.locator(EmployeeManagementLocators.SEARCH_INPUT)
            search_field.wait_for(state="visible")
            search_field.fill(email)
            self.page.wait_for_timeout(3000)  # Ожидание прогрузки

            # Открытие меню
            burger_menu = self.page.locator(EmployeeManagementLocators.BURGER_MENU)
            burger_menu.wait_for(state="visible")
            burger_menu.click()

            # Выбор удаления
            delete_option = self.page.locator(EmployeeManagementLocators.DELETE_OPTION)
            delete_option.wait_for(state="visible")
            delete_option.click()

            # Подтверждение удаления
            confirm_button = self.page.locator(EmployeeManagementLocators.CONFIRM_DELETE_BUTTON)
            confirm_button.wait_for(state="visible")
            confirm_button.click()

            # Ожидание завершения
            self.page.wait_for_load_state("networkidle")

        except Exception as e:
            raise

    def verify_delete_success(self):
        try:
            # Проверяем уведомление об успешном удалении
            if self.page.locator(EmployeeManagementLocators.SUCCESS_NOTIFICATION).count() > 0:
                notification = self.page.locator(EmployeeManagementLocators.SUCCESS_NOTIFICATION)
                notification.wait_for(state="visible")
                expect(notification).to_contain_text("Приглашение успешно удалено")

        except Exception as e:
            raise
