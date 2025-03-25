from playwright.sync_api import Page
from locators.import_ou_locators import ImportOULocators
from config.config import DEFAULT_TIMEOUT

class ImportOUPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_devices(self):
        """Переход в раздел устройств"""
        self.page.click(ImportOULocators.USER_MENU)
        self.page.click(ImportOULocators.DEVICES_MENU)
        self.page.wait_for_load_state("networkidle")

    def open_import_modal(self):
        """Открытие модального окна импорта"""
        self.page.click(ImportOULocators.IMPORT_AD_BUTTON)
        self.page.wait_for_selector(
            ImportOULocators.SERVER_INPUT,
            state="visible",
            timeout=DEFAULT_TIMEOUT*2
        )

    def fill_connection_details(self):
        """Заполнение данных подключения"""
        self.page.fill(ImportOULocators.SERVER_INPUT, "dc01.test.local")
        self.page.fill(ImportOULocators.USERNAME_INPUT, "user1")
        self.page.fill(ImportOULocators.PASSWORD_INPUT, "qwe")
        self.page.fill(ImportOULocators.QUERY_INPUT, "OU=Тестовые компы,DC=test,DC=local")

    def search_and_select_device(self):
        """Поиск и выбор устройства"""
        self.page.click(ImportOULocators.GET_DEVICES_BUTTON)
        self.page.wait_for_selector(
            ImportOULocators.SEARCH_INPUT,
            state="visible",
            timeout=DEFAULT_TIMEOUT*3
        )
        self.page.fill(ImportOULocators.SEARCH_INPUT, "238 811 384")
        self.page.keyboard.press('Enter')
        self.page.click(ImportOULocators.DEVICE_CHECKBOX)
        self.page.wait_for_selector(
            ImportOULocators.DEVICE_CHECKBOX,
            state="visible",
            timeout=DEFAULT_TIMEOUT*3
        )
    def perform_import(self):
        """Выполнение импорта"""
        self.page.click(ImportOULocators.IMPORT_BUTTON)
        self.page.click(ImportOULocators.CONFIRM_BUTTON)
        self.page.wait_for_selector(
            ImportOULocators.RESULT_MODAL,
            state="visible",
            timeout=DEFAULT_TIMEOUT*3
        )

    def verify_success(self):
        """Проверка результатов"""
        # Проверяем наличие элемента по заданному XPath
        element = self.page.locator(ImportOULocators.RESULT_MODAL)

        # Если элемент существует, тест считается успешным
        if element.count() > 0:
            print("Тест успешен: элемент найден.")
            return True
        else:
            print("Тест неуспешен: элемент не найден.")
            return False