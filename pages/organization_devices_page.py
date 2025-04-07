# pages/organization_devices_page.py

from playwright.sync_api import Page, expect
from locators.organization_device_locators import OrganizationDeviceLocators
import config


class OrganizationDevicesPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_organization_devices(self):
        self.page.goto(self.urls["dashboard_url"])
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(OrganizationDeviceLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Устройства'")
        self.page.click(OrganizationDeviceLocators.DEVICES_MENU)

    def delete_device(self):
        print("Удаляем устройство")
        self.page.click(OrganizationDeviceLocators.BURGER_DELETE_DEVICE)
        self.page.click(OrganizationDeviceLocators.DELETE_BUTTON)
        self.page.click(OrganizationDeviceLocators.CONFIRM_BUTTON)
        print("Устройство удалено")

    def add_device(self, device_id: str):
        print("Нажатие на кнопку 'Добавить устройство'")
        self.page.click(OrganizationDeviceLocators.ADD_DEVICE_BUTTON)
        print(f"Ввод идентификатора устройства: {device_id}")
        self.page.fill(OrganizationDeviceLocators.DEVICE_ID_INPUT, device_id)
        print("Нажатие на кнопку 'Сохранить'")
        self.page.click(OrganizationDeviceLocators.SAVE_DEVICE_BUTTON)
        self.page.click(OrganizationDeviceLocators.SAVE_DEVICE_BUTTON)

    def should_see_success_add_message(self):
        print("Проверка уведомления об успешном добавлении устройства")
        success_msg = self.page.locator(OrganizationDeviceLocators.SUCCESS_ADD_MSG)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()
