# locators/admin_devices_locators.py
class AdminDevicesLocators:
    ADMIN_MENU = "xpath=/html/body/div[1]/nav/div/ul/li[5]/a/span[1]"
    DEVICES_MENU = "xpath=/html/body/div[1]/nav/div/ul/li[5]/ul/li[1]/a"
    SEARCH_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/label/input"
    DEVICE_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/table/thead/tr/th[1]/input"
    ADD_TO_ORG_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/button[1]/i"
    ORG_SELECT_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div"
    ORG_OPTION = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/ul/li[3]/label"
    EXECUTE_BUTTON = "xpath=//button[contains(., 'Выполнить')]"
    SUCCESS_ALERT = "text=Успешно добавлено/обновлено 1 устройство."
