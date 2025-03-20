# locators/collection_locators.py

class CollectionLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    COLLECTIONS_MENU = "text=Коллекции"

    # Локаторы для кнопок бургера
    BURGER_BUTTON_DEVICE = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[4]/td[2]/div/div"
    BURGER_BUTTON_DOMAIN = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/div/i"
    BURGER_BUTTON_INVENTORY = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/div/i"

    SYNC_BUTTON_DEVICE = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[4]/td[2]/div/ul/li[3]/a"
    SYNC_BUTTON_DOMAIN = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/ul/li[3]/a"
    SYNC_BUTTON_INVENTORY = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/ul/li[3]/a"
    SUCCESS_MESSAGE = "text=Содержимое коллекции синхронизировано"
