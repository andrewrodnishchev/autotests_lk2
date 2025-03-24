import pytest
from pages.auth_page import AuthPage
from pages.category_page import CategoryPage
from config.config import ADMIN_LOGIN, ADMIN_PASSWORD

def test_category_management(page):
    auth_page = AuthPage(page)
    category_page = CategoryPage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(ADMIN_LOGIN, ADMIN_PASSWORD)

    # Основные шаги
    category_page.navigate_to_categories()

    # Создание категории
    category_page.create_category("Тестовая категория")

    # Редактирование категории
    category_page.edit_category("Тестовая категория", "Тестовая категория 2")

    # Удаление категории
    category_page.delete_category()