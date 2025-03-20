# locators/employee_locators.py

class EmployeeLocators:
    ORGANIZATION_MENU = "text=Тест Андрей"
    EMPLOYEES_MENU = "text=Сотрудники"
    SELECT_ALL_CHECKBOX = "#ClOrgUsrTab90 > thead > tr > th.check.details-control.sorting_disabled > input"  # Чекбокс "Выбрать всех"
    EDIT_BUTTON = "#editable_wrapper > div.control > button > i"
    LIST_DROPDOWN = "#DialogFormId > div > div:nth-child(1) > div > div > p > span"  # Выпадающий список
    NO_CHANGE_OPTION = "#DialogFormId > div > div:nth-child(1) > div > div > div > ul > li.opt.selected > label"  # Опция "Не изменять"
    EXECUTE_BUTTON = "text=Выполнить"
    SUCCESS_MESSAGE = "text=Успешно изменено сотрудников: 3"