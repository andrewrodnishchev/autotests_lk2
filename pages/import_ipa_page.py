from playwright.sync_api import Page, expect
from locators.import_ipa_locators import IPAImportLocators
import config


class IPAImportPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_devices_section(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(IPAImportLocators.ANDREY_TEST_BUTTON)
        self.page.click(IPAImportLocators.DEVICES_MENU_ITEM)

    def open_import_modal(self):
        self.page.click(IPAImportLocators.IMPORT_FROM_AD_BUTTON)

    def select_ipa_domain(self):
        dropdown = self.page.locator(IPAImportLocators.DOMAIN_DROPDOWN)

        # Явное ожидание появления dropdown
        dropdown.wait_for(state="visible", timeout=10000)

        # Используем более надежный метод выбора
        dropdown.select_option(
            value="IPA",  # Или index=1 если value недоступно
            timeout=5000
        )

    def fill_connection_details(self):
        self.page.fill(IPAImportLocators.DOMAIN_INPUT, "ipa.local")
        self.page.fill(IPAImportLocators.USERNAME_INPUT, "uid=savenko,cn=users,cn=accounts,dc=ipa,dc=local")
        self.page.fill(IPAImportLocators.PASSWORD_INPUT, "12345678")
