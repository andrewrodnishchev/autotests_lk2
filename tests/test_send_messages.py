# tests/test_send_messages.py

import pytest
from pages.auth_page import AuthPage
from pages.message_page import MessagePage
import config


@pytest.mark.regression
def test_send_message_to_devices(page, stand):
    auth_page = AuthPage(page)
    message_page = MessagePage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    message_page.navigate_to_organization_devices()
    message_page.select_checkboxes()
    message_page.send_message_to_devices("Тестовое сообщение")
    message_page.should_see_success_message()
