class ChangeStatusLocators:
    ADMIN_MENU = "xpath=/html/body/div[1]/nav/div/ul/li[5]/a"
    ACCOUNTS_MENU_ITEM = "xpath=/html/body/div[1]/nav/div/ul/li[5]/ul/li[6]/a"
    CHECKBOX_BY_EMAIL = "xpath=//tr[td[contains(@class, 's-align-left') and text()='{}']]//input[@class='js-chk']"

    CHANGE_STATUS_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/button[4]/i"
    STATUS_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div/div/p/span"
    STATUS_BLOCKED = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[1]/div/div/div/ul/li[2]/label"
    EXECUTE_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[2]/button[1]"
    SUCCESS_MODAL = "xpath=/html/body/div[4]/div/div/div"
