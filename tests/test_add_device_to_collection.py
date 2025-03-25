# tests/test_add_device_to_collection.py
import pytest
from pages.auth_page import AuthPage
from pages.device_collection_page import DeviceCollectionPage
import config


@pytest.mark.regression
def test_add_device_to_collection(page, stand):
    auth_page = AuthPage(page)
    device_collection_page = DeviceCollectionPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    device_collection_page.navigate_to_organization_collections()
    device_collection_page.add_device_to_collection("135026892")
    device_collection_page.should_see_success_message()
