import time

from playwright.sync_api import Page, expect
from locators.admin_page_locators import AdminPageLocators
import config


class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_administration(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(AdminPageLocators.ADMINISTRATION_TAB)
        self.page.wait_for_load_state("networkidle")

    def open_accounts(self):
        self.page.click(AdminPageLocators.ACCOUNTS_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_user(self, email: str):
        search_input = self.page.locator(AdminPageLocators.SEARCH_INPUT)
        search_input.fill(email)
        search_input.press("Enter")
        self.page.wait_for_load_state("networkidle")

        time.sleep(1)

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
            timeout=config.DEFAULT_TIMEOUT
        )
