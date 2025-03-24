from playwright.sync_api import Page, expect
from locators.admin_license_locators import AdminLicenseLocators
from config.config import DEFAULT_TIMEOUT

class AdminLicensePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_accounts(self):
        self.page.click(AdminLicenseLocators.ADMINISTRATION_TAB)
        self.page.click(AdminLicenseLocators.ACCOUNTS_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_user(self, email: str):
        search_input = self.page.locator(AdminLicenseLocators.SEARCH_INPUT)
        search_input.fill(email)
        search_input.press("Enter")  # Нажимаем Enter вместо ожидания
        self.page.wait_for_load_state("networkidle")  # Ждем завершения загрузки
        # Дополнительная проверка загрузки результатов
        self.page.wait_for_selector(AdminLicenseLocators.CHECKBOX, timeout=DEFAULT_TIMEOUT*2)

    def select_user(self):
        checkbox = self.page.locator(AdminLicenseLocators.CHECKBOX)
        checkbox.wait_for(state="visible")
        checkbox.check()

    def activate_license(self):
        self.page.click(AdminLicenseLocators.ACTIVATE_LICENSE_BUTTON)
        self.page.wait_for_selector(AdminLicenseLocators.LICENSE_DROPDOWN)

        self.page.click(AdminLicenseLocators.LICENSE_DROPDOWN)
        self.page.click(AdminLicenseLocators.LICENSE_OPTION)

        self.page.click(AdminLicenseLocators.ACTIVATE_BUTTON)

    def verify_success(self):
        success_msg = self.page.locator(AdminLicenseLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible")
        expect(success_msg).to_be_visible()