# locators/employee_management_locators.py
class EmployeeManagementLocators:
    # Основные элементы
    ORGANIZATION_LINK = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div/div[2]/a/h2"
    EMPLOYEES_SECTION = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/ul/li[5]/a"

    # Добавление сотрудника
    ADD_EMPLOYEE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[1]/a[1]"
    EMAIL_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[1]/div/div[2]/div/input"
    SAVE_BUTTON = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/form/div[3]/button"

    # Удаление сотрудника
    SEARCH_INPUT = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div/label/input"
    BURGER_MENU = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/div/i"
    DELETE_OPTION = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/table/tbody/tr/td[9]/div/ul/li[2]/a"
    CONFIRM_DELETE_BUTTON = "xpath=/html/body/div[4]/div[2]/div/div/div[2]/div/div/form/div[2]/button[1]"

    # Уведомления
    SUCCESS_NOTIFICATION = "xpath=//div[contains(@class, 'ant-notification-notice-success')]"
    ERROR_MESSAGE = "xpath=//div[contains(@class, 'ant-form-item-explain-error')]"
