import time

from playwright.sync_api import Page, expect
from locators.profile_locators import ProfileLicenseLocators
import config


class ProfileLicensePage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)
        self.stand = config.SELECTED_STAND  # Добавляем сохранение стенда

    def off_direct_control(self):
        self.page.click(ProfileLicenseLocators.ADMIN)
        self.page.click(ProfileLicenseLocators.SETTINGS)
        self.page.click(ProfileLicenseLocators.DIRECT_CONTROL)
        self.page.click(ProfileLicenseLocators.SAVE)

        time.sleep(2)

    def navigate_to_profile(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(ProfileLicenseLocators.USER_MENU)
        self.page.click(ProfileLicenseLocators.PROFILE_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def open_license_activation(self):
        self.page.click(ProfileLicenseLocators.ACTIVATE_BUTTON)
        self.page.wait_for_selector(
            ProfileLicenseLocators.LICENSE_INPUT,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )

    def activate_license(self, license_key: str):
        self.page.fill(ProfileLicenseLocators.LICENSE_INPUT, license_key)
        self.page.click(ProfileLicenseLocators.SUBMIT_BUTTON)
        success_modal = self.page.locator(ProfileLicenseLocators.SUCCESS_MODAL)
        success_modal.wait_for(state="visible", timeout=config.DEFAULT_TIMEOUT * 3)
        expect(success_modal).to_contain_text("Лицензия успешно активирована")

    def on_direct_control(self):
        self.page.click(ProfileLicenseLocators.ADMIN)
        self.page.click(ProfileLicenseLocators.SETTINGS)
        self.page.click(ProfileLicenseLocators.DIRECT_CONTROL)
        self.page.click(ProfileLicenseLocators.SAVE)
