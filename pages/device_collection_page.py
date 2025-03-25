# pages/device_collection_page.py

from playwright.sync_api import Page, expect
from locators.device_collection_locators import DeviceCollectionLocators
import config


class DeviceCollectionPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_organization_collections(self):
        self.page.goto(self.urls["dashboard_url"])
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(DeviceCollectionLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Коллекции'")
        self.page.click(DeviceCollectionLocators.COLLECTIONS_MENU)

    def add_device_to_collection(self, device_id: str):
        print("Нажатие на кнопку 'Добавить устройство'")
        self.page.click(DeviceCollectionLocators.ADD_DEVICE_BUTTON)
        print("Ожидание загрузки страницы добавления устройства")
        self.page.wait_for_load_state("networkidle")
        print(f"Ввод идентификатора устройства: {device_id}")
        self.page.fill(DeviceCollectionLocators.DEVICE_ID_INPUT, device_id)
        print("Нажатие на кнопку 'Сохранить'")
        self.page.click(DeviceCollectionLocators.SAVE_BUTTON)
        self.page.click(DeviceCollectionLocators.SAVE_BUTTON)

    def should_see_success_message(self):
        print("Проверка уведомления об успешном добавлении")
        success_msg = self.page.locator(DeviceCollectionLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()
