import time

from playwright.sync_api import Page, expect
from locators.device_license_locators import DeviceLicenseLocators
from config.config import DEFAULT_TIMEOUT

class DeviceLicensePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_devices(self):
        self.page.click(DeviceLicenseLocators.ADMINISTRATION_TAB)
        self.page.click(DeviceLicenseLocators.DEVICES_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_device(self, device_id: str):
        search_input = self.page.locator(DeviceLicenseLocators.SEARCH_INPUT)
        search_input.fill(device_id)
        search_input.press("Enter")
        self.page.wait_for_selector(
            DeviceLicenseLocators.CHECKBOX,
            state="visible",
            timeout=DEFAULT_TIMEOUT*2
        )


    def select_device(self):
        checkbox = self.page.locator(DeviceLicenseLocators.CHECKBOX)
        checkbox.click()


    def activate_license(self):
        self.page.click(DeviceLicenseLocators.ACTIVATE_BUTTON)


        # Работа с выпадающим списком
        self.page.click(DeviceLicenseLocators.LICENSE_DROPDOWN)
        self.page.click(DeviceLicenseLocators.LICENSE_OPTION)

        # Подтверждение активации
        self.page.click(DeviceLicenseLocators.CONFIRM_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_success(self):
        success_msg = self.page.locator(DeviceLicenseLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=DEFAULT_TIMEOUT*2)
        expect(success_msg).to_be_visible()