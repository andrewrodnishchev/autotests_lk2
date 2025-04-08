# pages/license_activation_page.py
from playwright.sync_api import Page, expect
from locators.license_activation_locators import LicenseActivationLocators
import config
import time


class LicenseActivationPage:
    def __init__(self, page: Page):
        self.page = page

    def go_to_admin_section(self):
        self.page.click(LicenseActivationLocators.ADMINISTRATION_BUTTON)
        self.page.click(LicenseActivationLocators.ACCOUNTS_MENU_ITEM)
        self.page.wait_for_load_state("networkidle")

    def search_account(self, email: str):
        """Поиск учётной записи по email"""
        search_field = self.page.locator(LicenseActivationLocators.SEARCH_INPUT)
        search_field.click()
        search_field.fill(email)
        search_field.press("Enter")
        time.sleep(2)  # Ждём обновления таблицы

    def open_account_actions_menu(self):
        """Открытие меню действий для найденной учётной записи"""
        self.page.locator(LicenseActivationLocators.ACCOUNT_ACTIONS_BUTTON).first.click()

    def activate_license_with_restriction(self):
        # Добавляем ожидание появления кнопки активации
        self.page.locator(LicenseActivationLocators.ACTIVATE_LICENSE_BUTTON).click(timeout=10000)

        # Ожидание и выбор опции
        dropdown = self.page.locator(LicenseActivationLocators.LICENSE_TYPE_DROPDOWN)
        self.page.click(LicenseActivationLocators.LICENSE_TYPE_DROPDOWN)
        self.page.click(LicenseActivationLocators.CORRECT_LICENSE)

        # Активация
        self.page.click(LicenseActivationLocators.ACTIVATE_SUBMIT_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def open_my_assistant(self):
        self.page.click(LicenseActivationLocators.MY_ASSISTANT_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def verify_devices_section_hidden(self):
        devices_section = self.page.locator(LicenseActivationLocators.DEVICES_SECTION)
        expect(devices_section).not_to_be_visible(timeout=config.DEFAULT_TIMEOUT * 2)
