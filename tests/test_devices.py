import pytest
from pages.auth_page import AuthPage
from pages.devices_page import DevicesPage
import config


@pytest.mark.regression
def test_device_workflow(page, stand):
    auth_page = AuthPage(page)
    devices_page = DevicesPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)
    auth_page.should_be_on_dashboard()

    devices_page.navigate_to_devices()
    devices_page.add_device("014 917 927")
    devices_page.should_see_success_add_message()
    devices_page.edit_device_comment("Тест")
    devices_page.should_see_success_save_message()
    devices_page.delete_device()
    devices_page.should_see_success_delete_message()
