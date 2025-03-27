# locators/license_page_locators.py

class LicensePageLocators:
    # Новый локатор для выбора организации
    ORGANIZATION_MENU = "text=тест андрей"

    USER_MENU = "text=Андрей Роднищев"
    EMPLOYEE_SECTION = "text=Сотрудник"
    CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/input"
    EDIT_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[1]/button/i"
    LICENSE_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[4]/div/div/select"
    ACTIVATE_OPTION = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[4]/div/div/select/option[3]"
    SECOND_DROPDOWN = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[5]/div/div/select"
    LICENSE_OPTION = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[5]/div/div/select/option[6]"
    EXECUTE_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/div[6]/button[1]"
    SUCCESS_MESSAGE = "text=Успешно изменено сотрудников: 1"
