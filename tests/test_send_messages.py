# tests/test_send_messages.py

import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.message_page import MessagePage

@pytest.mark.regression
def test_send_message_to_devices(page):
    auth_page = AuthPage(page)
    message_page = MessagePage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств организации
    message_page.navigate_to_organization_devices()

    # Выбор общего чекбокса
    message_page.select_checkboxes()

    # Отправка сообщения
    message_page.send_message_to_devices("Тестовое сообщение")

    # Проверка успешной отправки
    message_page.should_see_success_message()