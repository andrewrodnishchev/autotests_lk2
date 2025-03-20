import time

from playwright.sync_api import Page, expect
from locators.admin_page_locators import AdminPageLocators
from config.config import DEFAULT_TIMEOUT

class AdminPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_administration(self):
        self.page.click(AdminPageLocators.ADMINISTRATION_TAB)
        self.page.wait_for_load_state("networkidle")

    def open_accounts(self):
        self.page.click(AdminPageLocators.ACCOUNTS_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_user(self, email: str):
        # Вводим email и нажимаем Enter
        search_input = self.page.locator(AdminPageLocators.SEARCH_INPUT)
        search_input.fill(email)
        search_input.press("Enter")
        self.page.wait_for_load_state("networkidle")  # Ожидание завершения поиска

        time.sleep(3)

    def open_edit_menu(self):
        self.page.click(AdminPageLocators.BURGER_BUTTON)
        self.page.click(AdminPageLocators.EDIT_BUTTON)

    def update_email(self, new_email: str):
        email_field = self.page.locator(AdminPageLocators.EMAIL_INPUT)
        email_field.fill("")
        email_field.fill(new_email)

    def save_changes(self):
        self.page.click(AdminPageLocators.SAVE_BUTTON)

    def verify_success(self):
        expect(self.page.locator(AdminPageLocators.SUCCESS_MESSAGE)).to_be_visible(
            timeout=DEFAULT_TIMEOUT
        )