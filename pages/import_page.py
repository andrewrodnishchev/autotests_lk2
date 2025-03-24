import time

from playwright.sync_api import Page, expect
from locators.import_locators import ImportLocators
from config.config import DEFAULT_TIMEOUT

class ImportPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_devices(self):
        """Переход в раздел устройств"""
        self.page.click(ImportLocators.USER_MENU)
        self.page.click(ImportLocators.DEVICES_MENU)
        self.page.wait_for_load_state("networkidle")

    def open_import_modal(self):
        """Открытие модального окна импорта"""
        self.page.click(ImportLocators.IMPORT_AD_BUTTON)
        self.page.wait_for_selector(
            ImportLocators.MODAL_SERVER_INPUT,
            state="visible",
            timeout=DEFAULT_TIMEOUT*2
        )

    def fill_connection_form(self):
        """Заполнение формы подключения"""
        self.page.fill(ImportLocators.MODAL_SERVER_INPUT, "dc01.test.local")
        self.page.fill(ImportLocators.MODAL_USERNAME_INPUT, "user1")
        self.page.fill(ImportLocators.MODAL_PASSWORD_INPUT, "qwe")
        self.page.fill(ImportLocators.MODAL_QUERY_INPUT, "DC=test,DC=local")
        self.page.fill(ImportLocators.MODAL_FILTER_INPUT, "&(objectCategory=computer)(description=тест)")
        self.page.click(ImportLocators.DEVICE_LIST_BUTTON)

        time.sleep(5)

    def select_devices(self):
        self.page.fill(ImportLocators.ACCOUNT_INPUT, "238 811 384")

        # Клик по чекбоксу
        self.page.click(ImportLocators.DEVICE_CHECKBOX)

    def perform_import(self):
        """Выполнение импорта"""
        self.page.click(ImportLocators.IMPORT_BUTTON)
        self.page.click(ImportLocators.CONFIRM_BUTTON)
        self.page.wait_for_selector(
            ImportLocators.RESULT_MODAL,
            state="visible",
            timeout=DEFAULT_TIMEOUT*3
        )

    def verify_result(self):
        """Проверка результатов"""
    # Проверяем наличие элемента по заданному XPath
        element = self.page.locator(ImportLocators.RESULT_MODAL)

    # Если элемент существует, тест считается успешным
        if element.count() > 0:
            print("Тест успешен: элемент найден.")
            return True
        else:
            print("Тест неуспешен: элемент не найден.")
            return False