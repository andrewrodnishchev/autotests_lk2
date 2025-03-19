from playwright.sync_api import Page, expect
from locators.auth_page_locators import AuthPageLocators

class AuthPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login_page(self):
        self.page.goto("http://lk.corp.dev.ru/Account/Login?returnUrl=%2FClientOrg")

    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def enter_username(self, username: str):
        self.page.fill(AuthPageLocators.LOGIN_FIELD, username)

    def enter_password(self, password: str):
        self.page.fill(AuthPageLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        self.page.click(AuthPageLocators.LOGIN_BUTTON)

    def should_see_error_message(self):
        expect(self.page.locator(AuthPageLocators.ERROR_MESSAGE)).to_be_visible()

    def should_see_welcome_message(self):
        expect(self.page.locator(AuthPageLocators.WELCOME_MESSAGE).nth(0)).to_be_visible()

    def should_be_on_dashboard(self):
        expect(self.page).to_have_url("http://lk.corp.dev.ru/ClientOrg")