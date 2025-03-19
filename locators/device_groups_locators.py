class DeviceGroupsLocators:
    MY_ASSISTANT_MENU = "text=Мой ассистент"
    DEVICES_MENU = "text=Устройства"
    ADD_GROUP_BUTTON = "text=Добавить группу"
    GROUP_NAME_INPUT = "#Name"
    SAVE_BUTTON = "button:has-text('Сохранить')"
    SUCCESS_CREATE_MSG = "text=Группа устройств успешно создана"
    SUCCESS_EDIT_MSG = "text=Группа устройств успешно изменена"

    # Селектор для кнопки бургера (полный XPath)
    @staticmethod
    def get_burger_button():
        return "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/div/div/i"

    EDIT_BUTTON = "text=Изменить"
    DELETE_BUTTON = "text=Удалить"
    CONFIRM_DELETE_BUTTON = "button:has-text('Удалить')"

    @staticmethod
    def group_name_element(group_name: str):
        return f"text={group_name}"