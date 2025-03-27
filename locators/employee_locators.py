# locators/employee_locators.py

class EmployeeLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    EMPLOYEES_MENU = "text=Сотрудники"
    SELECT_ALL_CHECKBOX = "xpath=/html/body/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[4]/div/div/div[2]/div/div[2]/table/thead/tr/th[1]/input"  # Чекбокс "Выбрать всех"
    EDIT_BUTTON = "#editable_wrapper > div.control > button > i"
    LIST_DROPDOWN = "#DialogFormId > div > div:nth-child(1) > div > div > p > span"  # Выпадающий список
    NO_CHANGE_OPTION = "#DialogFormId > div > div:nth-child(1) > div > div > div > ul > li.opt.selected > label"  # Опция "Не изменять"
    EXECUTE_BUTTON = "text=Выполнить"
    SUCCESS_MESSAGE = "text=Успешно изменено сотрудников"
