from playwright.sync_api import Page, expect
from locators.device_import_locators import DeviceImportLocators
import config


class DeviceImportPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_organization(self):
        self.page.click(DeviceImportLocators.ORG_SELECTOR)
        self.page.wait_for_load_state("networkidle")

    def open_devices_section(self):
        self.page.click(DeviceImportLocators.DEVICES_MENU)
        self.page.wait_for_selector(
            DeviceImportLocators.IMPORT_AD_BUTTON,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT
        )

    def start_ad_import(self):
        self.page.click(DeviceImportLocators.IMPORT_AD_BUTTON)
        self.page.wait_for_selector(
            DeviceImportLocators.SERVER_INPUT,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT
        )

    def fill_connection_details(self, server: str, username: str, password: str):
        self.page.fill(DeviceImportLocators.SERVER_INPUT, server)
        self.page.fill(DeviceImportLocators.USERNAME_INPUT, username)
        self.page.fill(DeviceImportLocators.PASSWORD_INPUT, password)

    def submit_import(self):
        self.page.click(DeviceImportLocators.SUBMIT_IMPORT_BUTTON)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)  # Дополнительная задержка для стабильности

    def apply_registration_filter(self):
        try:
            # Открываем фильтр
            self.page.click(DeviceImportLocators.FILTER_BUTTON)
            self.page.wait_for_selector(
                DeviceImportLocators.REGISTRATION_DROPDOWN_TOGGLE,
                state="visible",
                timeout=config.DEFAULT_TIMEOUT * 2
            )

            # Открываем выпадающий список
            self.page.click(DeviceImportLocators.REGISTRATION_DROPDOWN_TOGGLE)

            # Выбираем опцию "Все"

            # Ставим чекбокс "Выбрать все"
            checkbox = self.page.locator(DeviceImportLocators.SELECT_ALL_CHECKBOX)
            self.page.click(DeviceImportLocators.SELECT_ALL_CHECKBOX)

            # Применяем фильтр
            self.page.click(DeviceImportLocators.APPLY_BUTTON)
            self.page.click(DeviceImportLocators.APPLY_BUTTON)

            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1000)

        except Exception as e:
            raise

    def verify_domain_present(self):
        domain_element = self.page.locator(DeviceImportLocators.RESULT_DOMAIN)
        expect(domain_element).to_be_visible(timeout=config.DEFAULT_TIMEOUT * 3)
