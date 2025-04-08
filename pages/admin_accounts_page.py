import time

from playwright.sync_api import Page, expect
from locators.admin_accounts_locators import AdminAccountsLocators
import config


class AdminAccountsPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_accounts(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(AdminAccountsLocators.ADMINISTRATION_TAB)
        self.page.click(AdminAccountsLocators.ACCOUNTS_MENU)
        self.page.wait_for_load_state("networkidle")

    def search_user(self, email: str):
        search_input = self.page.locator(AdminAccountsLocators.SEARCH_INPUT)
        search_input.fill(email)
        search_input.press("Enter")
        self.page.wait_for_selector(
            AdminAccountsLocators.CHECKBOX,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )

        time.sleep(2)

    def select_user(self):
        checkbox = self.page.locator(AdminAccountsLocators.CHECKBOX)
        checkbox.wait_for(state="visible")
        checkbox.click()

    def open_add_to_org_modal(self):
        self.page.click(AdminAccountsLocators.ADD_TO_ORG_BUTTON)
        self.page.wait_for_selector(
            AdminAccountsLocators.ORG_DROPDOWN,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )

    def select_organization(self):
        dropdown = self.page.locator(AdminAccountsLocators.ORG_DROPDOWN)
        dropdown.wait_for(state="visible", timeout=15000)
        dropdown.select_option(label="тест андрей", timeout=10000)

    # def toggle_checkbox(self):
    #     self.page.click(AdminAccountsLocators.TOGGLE_CHECKBOX)

    def execute_action(self):
        button = self.page.locator(AdminAccountsLocators.EXECUTE_BUTTON)
        button.wait_for(state="visible", timeout=10000)
        button.click()
        self.page.wait_for_load_state("networkidle")

    def verify_error(self):
        error_msg = self.page.locator(AdminAccountsLocators.ERROR_MESSAGE)
        error_msg.wait_for(state="visible", timeout=config.DEFAULT_TIMEOUT * 3)
        expect(error_msg).to_contain_text("Учетная запись andrey@mailforspam.com уже состоит")
