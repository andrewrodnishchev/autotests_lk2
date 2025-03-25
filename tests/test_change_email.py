import pytest
from pages.admin_page import AdminPage
from pages.auth_page import AuthPage
import config


def test_change_email(page, stand):
    auth_page = AuthPage(page)
    admin_page = AdminPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    admin_page.navigate_to_administration()
    admin_page.open_accounts()
    admin_page.search_user("rodnischev@safib.ru")
    admin_page.open_edit_menu()
    admin_page.update_email("rodnischev@safib.ru")
    admin_page.save_changes()
    admin_page.verify_success()
