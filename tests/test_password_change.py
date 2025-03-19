import pytest
from config.config import LOGIN, CORRECT_PASSWORD
from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage

@pytest.mark.regression
def test_password_change(page):
    # Авторизация
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()
    auth_page.login(LOGIN, CORRECT_PASSWORD)
    auth_page.should_be_on_dashboard()

    # Работа с профилем
    profile_page = ProfilePage(page)

    # Открываем меню профиля
    profile_page.open_profile_menu()

    # Переходим в профиль
    profile_page.navigate_to_profile()

    # Открываем вкладку безопасности
    profile_page.open_security_tab()

    # Открываем форму смены пароля
    profile_page.open_password_change_form()

    # Меняем пароль
    profile_page.change_password(
        old_pass=CORRECT_PASSWORD,
        new_pass=CORRECT_PASSWORD  # Здесь можно использовать новое значение
    )

    # Проверяем успешность операции
    profile_page.should_see_success_message()