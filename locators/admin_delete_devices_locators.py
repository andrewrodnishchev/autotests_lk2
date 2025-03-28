class AdminDeleteDevicesLocators:
    ADMIN_MENU = "xpath=/html/body/div[1]/nav/div/ul/li[5]/a/span[1]"
    DEVICES_MENU = "xpath=/html/body/div[1]/nav/div/ul/li[5]/ul/li[1]/a"
    SEARCH_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/label/input"
    DEVICE_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/table/thead/tr/th[1]/input"
    DELETE_BUTTON = "xpath=//button[contains(., 'Удалить')]"
    CONFIRM_MODAL_BUTTON = "xpath=//div[@role='dialog']//button[contains(., 'Удалить')]"
    SUCCESS_MODAL = "xpath=/html/body/div[4]/div/div/div"
