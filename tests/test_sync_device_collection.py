# tests/test_sync_device_collection.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage

@pytest.mark.regression
def test_sync_device_collection(page):
    auth_page = AuthPage(page)
    collection_page = CollectionPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел коллекций
    collection_page.navigate_to_organization_collections()

    # Синхронизация коллекции "Информация об устройстве"
    collection_page.sync_collection(collection_type="device")

    # Проверка уведомления
    collection_page.should_see_success_message()