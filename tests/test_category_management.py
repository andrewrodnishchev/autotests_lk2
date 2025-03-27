from pages.auth_page import AuthPage
from pages.category_page import CategoryPage
import config


def test_category_management(page, stand):
    auth_page = AuthPage(page)
    category_page = CategoryPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    category_page.navigate_to_categories()
    category_page.create_category("Тестовая категория")
    category_page.edit_category("Тестовая категория", "Тестовая категория 2")
    category_page.delete_category()
