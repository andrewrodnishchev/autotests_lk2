# pages/bulk_edit_page.py
import time

from playwright.sync_api import Page, expect
from locators.bulk_edit_locators import BulkEditLocators
import config


class BulkEditPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_organization_devices(self):
        self.page.goto(self.urls["dashboard_url"])
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(BulkEditLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Устройства'")
        self.page.click(BulkEditLocators.DEVICES_MENU)
        time.sleep(1)

    def select_device_checkbox(self):
        print("Выбор чекбокса устройства")
        checkbox = self.page.locator(BulkEditLocators.DEVICE_CHECKBOX)
        checkbox.wait_for(state="visible", timeout=10000)
        checkbox.click()

    def open_edit_menu(self):
        print("Нажатие на кнопку 'Изменить'")
        edit = self.page.locator(BulkEditLocators.EDIT_BUTTON)
        edit.wait_for(state="visible", timeout=10000)
        edit.click()

    def select_inventory_policy(self):
        print("Выбор политики инвентаризации")
        self.page.click(BulkEditLocators.POLICY_DROPDOWN)
        policy_option = self.page.locator(BulkEditLocators.POLICY_OPTION).first
        policy_option.wait_for(state="visible", timeout=10000)
        policy_option.click()

    def execute_changes(self):
        print("Нажатие на кнопку 'Выполнить'")
        self.page.click(BulkEditLocators.EXECUTE_BUTTON)
        self.page.wait_for_timeout(3000)

    def should_see_success_message(self):
        print("Проверка уведомления об успешном изменении")
        success_msg = self.page.locator(BulkEditLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()
