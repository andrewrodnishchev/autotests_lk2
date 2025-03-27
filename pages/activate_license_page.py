# pages/activate_license_page.py

import config
from playwright.sync_api import Page, expect
from locators.license_page_locators import LicensePageLocators


class LicensePage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_employee_section(self):
        # Выбираем организацию
        self.page.click(LicensePageLocators.ORGANIZATION_MENU)
        self.page.wait_for_load_state("networkidle")
        self.page.click(LicensePageLocators.EMPLOYEE_SECTION)
        self.page.wait_for_load_state("networkidle")

    def navigate_to_organization_devices(self):
        self.page.goto(f"{self.urls['dashboard_url']}/devices")
        self.page.wait_for_load_state("networkidle")

    # Остальные методы остаются без изменений, но должны использовать self.urls

    def select_employee(self):
        checkbox = self.page.locator(LicensePageLocators.CHECKBOX)
        checkbox.wait_for(state="visible", timeout=config.DEFAULT_TIMEOUT)  # Явное ожидание
        checkbox.check()

    def open_edit_menu(self):
        self.page.click(LicensePageLocators.EDIT_BUTTON)
        self.page.wait_for_selector(
            LicensePageLocators.LICENSE_DROPDOWN,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT
        )

    def select_license(self):
        # Явные ожидания для выпадающих списков
        self.page.locator(LicensePageLocators.LICENSE_DROPDOWN).wait_for(state="visible")
        self.page.select_option(LicensePageLocators.LICENSE_DROPDOWN, index=2)

        self.page.locator(LicensePageLocators.SECOND_DROPDOWN).wait_for(state="visible")
        self.page.select_option(LicensePageLocators.SECOND_DROPDOWN, index=2)

    def execute_changes(self):
        self.page.click(LicensePageLocators.EXECUTE_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_success(self):
        expect(self.page.locator(LicensePageLocators.SUCCESS_MESSAGE)).to_be_visible(
            timeout=config.DEFAULT_TIMEOUT * 2  # Увеличиваем таймаут для сообщения
        )
