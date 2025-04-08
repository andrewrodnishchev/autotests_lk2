# locators/license_activation_locators.py
class LicenseActivationLocators:
    # Основные элементы
    ADMINISTRATION_BUTTON = "xpath=//span[contains(text(),'Администрирование')]"
    ACCOUNTS_MENU_ITEM = "xpath=//a[contains(text(),'Учетные записи')]"

    # Поиск учётной записи
    SEARCH_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/div[1]/div/label/input"

    # Работа с учетной записью
    ACCOUNT_ACTIONS_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/div/i"
    ACTIVATE_LICENSE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[2]/table/tbody/tr/td[8]/div/ul/li[1]/a"

    # Модальное окно активации
    LICENSE_TYPE_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[1]/div[1]/div/div/p/label/i"
    ACTIVATE_SUBMIT_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]"
    CORRECT_LICENSE = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/ul/li[2]"
    # Раздел "Мой ассистент"
    MY_ASSISTANT_BUTTON = "xpath=//span[contains(text(), 'Мой ассистент')]"
    DEVICES_SECTION = "xpath=//a[contains(text(), 'Устройства')]"
