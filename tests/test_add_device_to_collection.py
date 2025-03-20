# tests/test_add_device_to_collection.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.device_collection_page import DeviceCollectionPage

@pytest.mark.regression
def test_add_device_to_collection(page):
    auth_page = AuthPage(page)
    device_collection_page = DeviceCollectionPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел коллекций
    device_collection_page.navigate_to_organization_collections()

    # Добавление устройства
    device_collection_page.add_device_to_collection("135026892")

    # Проверка уведомления
    device_collection_page.should_see_success_message()