class ProfileLicenseLocators:
    ADMIN = "xpath=/html/body/div[1]/nav/div/ul/li[5]/a"
    SETTINGS = "xpath=/html/body/div[1]/nav/div/ul/li[5]/ul/li[8]/a"
    DIRECT_CONTROL = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/form/div[1]/div/div[1]/div/div[1]/div[2]/div[1]/div/div/div/ins"
    SAVE = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/form/div[2]/button"

    USER_MENU = "xpath=//span[contains(text(), 'Андрей Роднищев')]"
    PROFILE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[1]/div/nav/ul/li/div/div[2]/a[1]"
    ACTIVATE_BUTTON = "text=Активировать"
    LICENSE_INPUT = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[1]/input"
    SUBMIT_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]"
    SUCCESS_MODAL = "xpath=/html/body/div[4]/div/div/div"
