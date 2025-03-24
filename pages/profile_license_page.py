from playwright.sync_api import Page, expect
from locators.profile_locators import ProfileLicenseLocators
from config.config import DEFAULT_TIMEOUT

class ProfileLicensePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_profile(self):
        """Переход в профиль пользователя"""
        self.page.click(ProfileLicenseLocators.USER_MENU)
        self.page.click(ProfileLicenseLocators.PROFILE_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def open_license_activation(self):
        """Открытие формы активации лицензии"""
        self.page.click(ProfileLicenseLocators.ACTIVATE_BUTTON)
        self.page.wait_for_selector(
            ProfileLicenseLocators.LICENSE_INPUT,
            state="visible",
            timeout=DEFAULT_TIMEOUT*2
        )

    def activate_license(self, license_key: str):
        """Активация лицензии"""
        self.page.fill(ProfileLicenseLocators.LICENSE_INPUT, license_key)
        self.page.click(ProfileLicenseLocators.SUBMIT_BUTTON)

        # Ожидание и проверка успешной активации
        success_modal = self.page.locator(ProfileLicenseLocators.SUCCESS_MODAL)
        success_modal.wait_for(state="visible", timeout=DEFAULT_TIMEOUT*3)
        expect(success_modal).to_contain_text("Лицензия успешно активирована")