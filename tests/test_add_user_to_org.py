from pages.auth_page import AuthPage
from pages.admin_accounts_page import AdminAccountsPage
import config


def test_add_user_to_organization(page, stand):
    auth_page = AuthPage(page)
    admin_page = AdminAccountsPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)

    admin_page.navigate_to_accounts()
    admin_page.search_user("andrey@mailforspam.com")
    admin_page.select_user()
    admin_page.open_add_to_org_modal()
    admin_page.select_organization()
    admin_page.toggle_checkbox()
    admin_page.execute_action()
    admin_page.verify_error()
