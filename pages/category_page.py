# pages/category_page.py
from playwright.sync_api import Page, expect
from locators.category_locators import CategoryLocators
import config


class CategoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_categories(self):
        self.page.goto(self.urls["dashboard_url"])
        print("ШАГ 1: Переход в раздел Администрирование -> Категории заявок")
        self.page.click(CategoryLocators.ADMINISTRATION_TAB)
        self.page.click(CategoryLocators.CATEGORIES_MENU)
        self.page.wait_for_load_state("networkidle")
        print("Успешный переход в раздел категорий")

    def create_category(self, name: str):
        print(f"\nШАГ 2: Создание категории '{name}'")
        print("Нажатие кнопки 'Создать'")
        self.page.click(CategoryLocators.CREATE_BUTTON)
        print(f"Ввод названия категории: {name}")
        self.page.fill(CategoryLocators.NAME_INPUT, name)
        print("Сохранение категории")
        self.page.click(CategoryLocators.SAVE_BUTTON)
        print("Ожидание сообщения об успехе")
        self.page.wait_for_selector(
            CategoryLocators.SUCCESS_MODAL,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )
        print("Категория успешно создана")

    def edit_category(self, old_name: str, new_name: str):
        print(f"\nШАГ 3: Изменение категории с '{old_name}' на '{new_name}'")
        print("Открытие контекстного меню категории")
        self.page.click(CategoryLocators.BURGER_BUTTON)
        self.page.click(CategoryLocators.EDIT_OPTION)
        print("Очистка поля ввода")
        name_input = self.page.locator(CategoryLocators.NAME_INPUT)
        name_input.fill("")
        print(f"Ввод нового названия: {new_name}")
        name_input.fill(new_name)
        print("Сохранение изменений")
        self.page.click(CategoryLocators.SAVE_BUTTON)
        print("Ожидание сообщения об успешном изменении")
        self.page.wait_for_selector(
            CategoryLocators.SUCCESS_MODAL,
            state="visible",
            timeout=config.DEFAULT_TIMEOUT * 2
        )
        print("Категория успешно изменена")

    def delete_category(self):
        print("\nШАГ 4: Удаление категории")
        print("Открытие контекстного меню")
        self.page.click(CategoryLocators.BURGER_BUTTON)
        self.page.click(CategoryLocators.DELETE_OPTION)
        print("Подтверждение удаления")
        self.page.click(CategoryLocators.CONFIRM_DELETE_BUTTON)
        print("Ожидание сообщения об удалении")
        self.page.wait_for_selector(
            CategoryLocators.DELETE_SUCCESS_MESSAGE,
            state="visible"
        )
        print("Категория успешно удалена")
