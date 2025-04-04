# tests/test_organization_devices.py

import pytest
from pages.auth_page import AuthPage
from pages.organization_devices_page import OrganizationDevicesPage
import config


@pytest.mark.regression
def test_add_device_to_organization(page, stand):
    auth_page = AuthPage(page)
    org_devices_page = OrganizationDevicesPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    org_devices_page.navigate_to_organization_devices()
    org_devices_page.add_device("027478388")
    org_devices_page.should_see_success_add_message()
