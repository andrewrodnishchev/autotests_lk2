from playwright.sync_api import Page, expect
from locators.auth_page_locators import AuthPageLocators
import config


class AuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_login_page(self):
        self.page.goto(self.urls["login_url"])

    def login(self, username: str, password: str):
        self.page.fill(AuthPageLocators.LOGIN_FIELD, username)
        self.page.fill(AuthPageLocators.PASSWORD_FIELD, password)
        self.page.click(AuthPageLocators.LOGIN_BUTTON)
        self.page.wait_for_url(self.urls["dashboard_url"])

    def should_be_on_dashboard(self):
        expect(self.page).to_have_url(self.urls["dashboard_url"])
