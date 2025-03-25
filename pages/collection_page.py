# pages/collection_page.py
from playwright.sync_api import Page, expect
from locators.collection_locators import CollectionLocators
import config


class CollectionPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_organization_collections(self):
        self.page.goto(self.urls["dashboard_url"])
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(CollectionLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Коллекции'")
        self.page.click(CollectionLocators.COLLECTIONS_MENU)

    def sync_collection(self, collection_type: str):
        burger_locator = {
            "device": CollectionLocators.BURGER_BUTTON_DEVICE,
            "domain": CollectionLocators.BURGER_BUTTON_DOMAIN,
            "inventory": CollectionLocators.BURGER_BUTTON_INVENTORY
        }[collection_type]

        print(f"Нажатие на кнопку бургера у коллекции: {collection_type}")
        burger_button = self.page.locator(burger_locator)
        burger_button.wait_for(state="visible", timeout=10000)
        burger_button.click()

        sync_locator = {
            "device": CollectionLocators.SYNC_BUTTON_DEVICE,
            "domain": CollectionLocators.SYNC_BUTTON_DOMAIN,
            "inventory": CollectionLocators.SYNC_BUTTON_INVENTORY
        }[collection_type]

        print("Нажатие на кнопку 'Синхронизировать'")
        sync_button = self.page.locator(sync_locator)
        sync_button.wait_for(state="visible", timeout=10000)
        sync_button.click()

    def should_see_success_message(self):
        print("Проверка уведомления об успешной синхронизации")
        success_msg = self.page.locator(CollectionLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()
