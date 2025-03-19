import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.device_groups_page import DeviceGroupsPage

@pytest.mark.regression
def test_device_groups_workflow(page):
    auth_page = AuthPage(page)
    groups_page = DeviceGroupsPage(page)

    # Авторизация
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Переход в раздел устройств
    groups_page.navigate_to_devices()

    # Создание группы
    original_name = groups_page.generate_unique_group_name()
    groups_page.create_group(original_name)
    groups_page.should_see_success_create_message()

    # Редактирование группы
    updated_name = f"{original_name} (2)"
    groups_page.edit_group(original_name, updated_name)
    groups_page.should_see_success_edit_message()

    # Удаление группы
    groups_page.delete_group(updated_name)
    groups_page.should_not_see_group(updated_name)