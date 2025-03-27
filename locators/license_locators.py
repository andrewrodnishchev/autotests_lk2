# locators/license_locators.py

class LicenseLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    DEVICES_MENU = "#page-wrapper-body > div.wrapper.wrapper-content > div > div.tabs-container > ul > li:nth-child(2) > a"
    DEVICE_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[2]/td[1]/input"  # Локатор для чекбокса устройства
    ACTIVATE_LICENSE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/button[5]"
    LICENSE_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[1]/div[1]/div/div"  # Локатор для выпадающего списка
    LICENSE_OPTION = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[1]/div[1]/div/div/div/ul/li[3]/label"  # Локатор для конкретной лицензии
    ACTIVATE_BUTTON = "button:has-text('Активировать')"
    SUCCESS_MESSAGE = "text=Лицензия успешно активирована на выбранных устройствах (1 шт.)"
