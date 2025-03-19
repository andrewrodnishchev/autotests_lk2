# locators/bulk_edit_locators.py

class BulkEditLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    DEVICES_MENU = "#page-wrapper-body > div.wrapper.wrapper-content > div > div.tabs-container > ul > li:nth-child(2) > a"
    DEVICE_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]/label[1]"  # Локатор чекбокса
    EDIT_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/button[2]/i"  # Кнопка "Изменить"
    POLICY_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[3]/div/div/p/span"  # Выпадающий список политики
    POLICY_OPTION = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/ul/li[3]/label"  # Пример опции
    EXECUTE_BUTTON = "#idBtnOk"  # Кнопка "Выполнить"
    SUCCESS_MESSAGE = "text=Успешно изменено устройств: 4"  # Уведомление