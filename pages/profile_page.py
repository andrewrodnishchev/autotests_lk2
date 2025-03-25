from playwright.sync_api import Page, expect
from locators.auth_page_locators import ProfilePageLocators
import config


class ProfilePage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def open_profile_menu(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(ProfilePageLocators.USER_MENU)

    def navigate_to_profile(self):
        self.page.wait_for_selector(ProfilePageLocators.PROFILE_BUTTON, state="visible", timeout=5000)
        self.page.click(ProfilePageLocators.PROFILE_BUTTON)

    def open_security_tab(self):
        self.page.click(ProfilePageLocators.SECURITY_TAB)

    def open_password_change_form(self):
        self.page.click(ProfilePageLocators.CHANGE_PASSWORD_BUTTON)

    def change_password(self, old_pass: str, new_pass: str):
        self.page.fill(ProfilePageLocators.OLD_PASSWORD_FIELD, old_pass)
        self.page.fill(ProfilePageLocators.NEW_PASSWORD_FIELD, new_pass)
        self.page.fill(ProfilePageLocators.CONFIRM_PASSWORD_FIELD, new_pass)
        self.page.click(ProfilePageLocators.SAVE_PASSWORD_BUTTON)

    def should_see_success_message(self):
        expect(self.page.locator(ProfilePageLocators.SUCCESS_MESSAGE)).to_be_visible()
