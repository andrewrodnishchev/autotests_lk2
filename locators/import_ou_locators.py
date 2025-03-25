class ImportOULocators:
    # Основные элементы
    USER_MENU = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/a/h2"
    DEVICES_MENU = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/ul/li[2]/a"
    IMPORT_AD_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/a[2]/i"

    # Модальное окно подключения
    SERVER_INPUT = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[1]/div[2]/div/input"
    USERNAME_INPUT = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[1]/div[3]/div/input"
    PASSWORD_INPUT = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[1]/div[4]/div/input"
    QUERY_INPUT = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[1]/div[5]/div/div/input"
    GET_DEVICES_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[2]/button[1]"

    # Работа со списком устройств
    SEARCH_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/label/input"
    DEVICE_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/table/tbody/tr[4]/td[1]/span"  # Локатор для чекбокса устройства
    IMPORT_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/div[1]/button/i"

    # Подтверждение импорта
    CONFIRM_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/form/div[2]/button[1]"
    RESULT_MODAL = "xpath=/html/body/div[4]/div[2]/div/div[1]/div[2]/form/div/div[2]/div[2]/div"
    SUCCESS_TEXT = "text=Успешно добавлено/обновлено устройств: 0"