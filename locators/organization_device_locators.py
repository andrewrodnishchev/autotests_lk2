# locators/organization_device_locators.py

class OrganizationDeviceLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"  # Локатор для выбора организации
    DEVICES_MENU = "#page-wrapper-body > div.wrapper.wrapper-content > div > div.tabs-container > ul > li:nth-child(2) > a"  # Локатор для перехода в раздел устройств
    ADD_DEVICE_BUTTON = "#editable_wrapper > div.control.mycontrol > div > a:nth-child(1) > i"  # Локатор для кнопки "Добавить устройство"
    DEVICE_ID_INPUT = "#HID"  # Локатор для поля ввода идентификатора устройства
    SAVE_DEVICE_BUTTON = "button:has-text('Сохранить')"  # Локатор для кнопки "Сохранить"
    SUCCESS_ADD_MSG = "text=Устройство успешно добавлено в организацию"  # Локатор для уведомления об успешном добавлении
    BURGER_DELETE_DEVICE = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/input"
    DELETE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/button[3]"
    CONFIRM_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[3]/button[1]"
