# tests/test_sync_domain_collection.py

import pytest
from pages.auth_page import AuthPage
from pages.collection_page import CollectionPage
import config


@pytest.mark.regression
def test_sync_domain_collection(page, stand):
    auth_page = AuthPage(page)
    collection_page = CollectionPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    collection_page.navigate_to_organization_collections()
    collection_page.sync_collection(collection_type="domain")
    collection_page.should_see_success_message()
