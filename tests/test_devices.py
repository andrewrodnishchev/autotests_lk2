import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.devices_page import DevicesPage

@pytest.mark.regression
def test_device_workflow(page):
    auth_page = AuthPage(page)
    devices_page = DevicesPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств
    devices_page.navigate_to_devices()

    # Добавление устройства
    devices_page.add_device("135026892")
    devices_page.should_see_success_add_message()

    # Редактирование комментария
    devices_page.edit_device_comment("Тест")
    devices_page.should_see_success_save_message()

    # Удаление устройства
    devices_page.delete_device()
    devices_page.should_see_success_delete_message()