from playwright.sync_api import Page, expect
from locators.admin_delete_devices_locators import AdminDeleteDevicesLocators
import config


class AdminDeleteDevicesPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_devices_section(self):
        self.page.click(AdminDeleteDevicesLocators.ADMIN_MENU)
        self.page.click(AdminDeleteDevicesLocators.DEVICES_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_device(self, device_id: str):
        search_field = self.page.locator(AdminDeleteDevicesLocators.SEARCH_INPUT)
        search_field.fill(device_id)
        search_field.press("Enter")
        self.page.wait_for_timeout(2000)

    def select_device(self):
        checkbox = self.page.locator(AdminDeleteDevicesLocators.DEVICE_CHECKBOX)
        checkbox.check(force=True)

    def delete_device(self):
        self.page.click(AdminDeleteDevicesLocators.DELETE_BUTTON)
        self.page.wait_for_selector(
            AdminDeleteDevicesLocators.CONFIRM_MODAL_BUTTON,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )
        self.page.click(AdminDeleteDevicesLocators.CONFIRM_MODAL_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_deletion_success(self):
        success_modal = self.page.locator(AdminDeleteDevicesLocators.SUCCESS_MODAL)
        success_modal.wait_for(state="visible", timeout=config.DEFAULT_TIMEOUT * 3)
        expect(success_modal).to_be_visible()
