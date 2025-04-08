# pages/admin_devices_page.py
from playwright.sync_api import Page, expect
from locators.admin_devices_locators import AdminDevicesLocators
import config


class AdminDevicesPage:
    def __init__(self, page: Page):
        self.page = page

    def delete_device(self):
        self.page.click(AdminDevicesLocators.ORGANIZATION)
        self.page.click(AdminDevicesLocators.DEVICES)
        self.page.click(AdminDevicesLocators.BURGER_DEVICE)
        self.page.click(AdminDevicesLocators.BURGER_DELETE_DEVICE)
        self.page.click(AdminDevicesLocators.CONFIRM_DELETE_DEVICE)

    def navigate_to_devices_section(self):
        self.page.click(AdminDevicesLocators.ADMIN_MENU)
        self.page.click(AdminDevicesLocators.DEVICES_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_device(self, device_id: str):
        search_field = self.page.locator(AdminDevicesLocators.SEARCH_INPUT)
        search_field.fill(device_id)
        search_field.press("Enter")
        self.page.wait_for_timeout(2000)  # Заменить на ожидание элемента

    def select_device(self):
        checkbox = self.page.locator(AdminDevicesLocators.DEVICE_CHECKBOX)
        checkbox.check(force=True)

    def add_to_organization(self):
        self.page.click(AdminDevicesLocators.ADD_TO_ORG_BUTTON)
        self.page.click(AdminDevicesLocators.EXECUTE_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_success(self):
        success_alert = self.page.locator(AdminDevicesLocators.SUCCESS_ALERT)
        expect(success_alert).to_contain_text(
            "Успешно добавлено/обновлено 1 устройство",
            timeout=config.DEFAULT_TIMEOUT * 3
        )
