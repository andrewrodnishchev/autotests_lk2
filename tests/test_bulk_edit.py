# tests/test_bulk_edit.py
import pytest
from pages.auth_page import AuthPage
from pages.bulk_edit_page import BulkEditPage
import config


@pytest.mark.regression
def test_bulk_edit_devices(page, stand):
    auth_page = AuthPage(page)
    bulk_edit_page = BulkEditPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    bulk_edit_page.navigate_to_organization_devices()
    bulk_edit_page.select_device_checkbox()
    bulk_edit_page.open_edit_menu()
    bulk_edit_page.select_inventory_policy()
    bulk_edit_page.execute_changes()
    bulk_edit_page.should_see_success_message()
