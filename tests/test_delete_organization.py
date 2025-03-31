import pytest
from pages.auth_page import AuthPage
from pages.organization_page import OrganizationPage
import config


def test_delete_organization(page, stand):
    auth_page = AuthPage(page)
    org_page = OrganizationPage(page)  # Теперь передаем page правильно
    test_org_name = "тест андрей 2"

    try:
        # Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

        # Явное ожидание загрузки страницы
        page.wait_for_load_state("networkidle")

        # Создание организации
        org_page.create_organization(test_org_name)

        # Явное ожидание перед удалением
        page.wait_for_load_state("networkidle")

        # Удаление организации
        org_page.delete_organization()

    except Exception as e:
        page.screenshot(path=f"delete_org_error_{stand}.png")
        pytest.fail(f"Ошибка удаления организации на стенде {stand}: {str(e)}")
