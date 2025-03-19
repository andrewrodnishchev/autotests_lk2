from playwright.sync_api import Page, expect
from locators.device_groups_locators import DeviceGroupsLocators
from datetime import datetime

class DeviceGroupsPage:
    def __init__(self, page: Page):
        self.page = page

    def generate_unique_group_name(self):
        return f"Тестовая группа {datetime.now().strftime('%d.%m.%Y %H:%M')}"

    def navigate_to_devices(self):
        print("Переход в раздел 'Мой ассистент'")
        self.page.click(DeviceGroupsLocators.MY_ASSISTANT_MENU)

        print("Переход в раздел 'Устройства'")
        self.page.click(DeviceGroupsLocators.DEVICES_MENU)

    def create_group(self, group_name: str):
        print("Нажатие на кнопку 'Добавить группу'")
        self.page.click(DeviceGroupsLocators.ADD_GROUP_BUTTON)

        print("Ожидание появления поля ввода 'Наименование'")
        group_name_input = self.page.locator(DeviceGroupsLocators.GROUP_NAME_INPUT)
        group_name_input.wait_for(state="visible", timeout=10000)

        print(f"Заполнение поля ввода названием: {group_name}")
        group_name_input.fill(group_name)

        print("Нажатие на кнопку 'Сохранить'")
        self.page.click(DeviceGroupsLocators.SAVE_BUTTON)

    def edit_group(self, group_name: str, new_name: str):
        print(f"Поиск кнопки бургера для группы: {group_name}")

    # Используем полный XPath для поиска кнопки бургера
        burger_button = self.page.locator(DeviceGroupsLocators.get_burger_button())

    # Ожидание появления кнопки бургера
        burger_button.wait_for(state="visible", timeout=20000)  # Увеличенное время ожидания

        print("Кнопка бургера найдена, выполняется клик")
        burger_button.click()

        print("Открытие формы редактирования")
        self.page.click(DeviceGroupsLocators.EDIT_BUTTON)

        print("Ожидание появления поля ввода 'Наименование'")
        group_name_input = self.page.locator(DeviceGroupsLocators.GROUP_NAME_INPUT)
        group_name_input.wait_for(state="visible", timeout=10000)

        print(f"Изменение названия группы на: {new_name}")
        group_name_input.fill(new_name)

        print("Нажатие на кнопку 'Сохранить'")
        self.page.click(DeviceGroupsLocators.SAVE_BUTTON)

    def delete_group(self, group_name: str):
        print(f"Поиск кнопки бургера для группы: {group_name}")
        burger_button = self.page.locator(DeviceGroupsLocators.get_burger_button())
        burger_button.wait_for(state="visible", timeout=20000)

        print("Кнопка бургера найдена, выполняется клик")
        burger_button.click()

        print("Нажатие на кнопку 'Удалить'")
        self.page.click(DeviceGroupsLocators.DELETE_BUTTON)

        print("Подтверждение удаления")
        self.page.click(DeviceGroupsLocators.CONFIRM_DELETE_BUTTON)

    def should_see_success_create_message(self):
        print("Проверка сообщения об успешном создании группы")
        expect(self.page.locator(
            DeviceGroupsLocators.SUCCESS_CREATE_MSG)).to_be_visible()

    def should_see_success_edit_message(self):
        print("Проверка сообщения об успешном изменении группы")
        expect(self.page.locator(
            DeviceGroupsLocators.SUCCESS_EDIT_MSG)).to_be_visible()

    def should_not_see_group(self, group_name: str):
        print(f"Проверка, что группа '{group_name}' удалена")
        expect(self.page.locator(
            DeviceGroupsLocators.group_name_element(group_name))).to_have_count(0)