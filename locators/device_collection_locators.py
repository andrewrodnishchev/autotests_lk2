# locators/device_collection_locators.py

class DeviceCollectionLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    COLLECTIONS_MENU = "text=Коллекции"
    ADD_DEVICE_BUTTON = "#editable_wrapper > div.control.mycontrol > div > a:nth-child(1)"  # Кнопка "Добавить устройство"
    DEVICE_ID_INPUT = "#HID"  # Поле "Идентификатор"
    SAVE_BUTTON = "button:has-text('Сохранить')"  # Кнопка "Сохранить"
    SUCCESS_MESSAGE = "text=Устройство успешно добавлено в коллекцию"  # Уведомление