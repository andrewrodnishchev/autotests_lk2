# locators/message_locators.py

class MessageLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    DEVICES_MENU = "#page-wrapper-body > div.wrapper.wrapper-content > div > div.tabs-container > ul > li:nth-child(2) > a"  # Локатор для перехода в раздел устройств
    MAIN_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]/label[1]"  # Локатор для всех чекбоксов в таблице
    SEND_MESSAGE_BUTTON = "#editable_wrapper > div.control.mycontrol > div > button:nth-child(6) > i"
    MESSAGE_INPUT = "#Text"
    SEND_SUBMIT_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]"
    SUCCESS_MESSAGE = "#toast-container > div > div > div"