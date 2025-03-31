import pytest
from pages.auth_page import AuthPage
from pages.change_status_page import ChangeStatusPage
import config
import time

TEST_ACCOUNTS = [
    "andrey@mailforspam.com",
    "ast1@mailforspam.com"
]


def test_change_status_selection(page, stand):
    auth_page = AuthPage(page)
    status_page = ChangeStatusPage(page)

    try:
        # Авторизация
        auth_page.navigate_to_login_page()
        auth_page.login(config.ADMIN_LOGIN, config.ADMIN_PASSWORD)
        time.sleep(2)

        # Открытие раздела
        status_page.open_accounts_section()

        # 1. Выбираем учетные записи
        print("Выбираем учетные записи...")
        status_page.select_accounts(TEST_ACCOUNTS)

        # 2. Меняем статус на "Заблокирован"
        print("Изменяем статус на 'Заблокирован'...")
        status_page.change_status_to_blocked(len(TEST_ACCOUNTS))

        # 3. Повторно выбираем те же учетные записи
        print("Повторно выбираем учетные записи...")
        status_page.select_accounts(TEST_ACCOUNTS)

        # 4. Возвращаем исходный статус
        print("Возвращаем исходный статус...")
        status_page.revert_status_changes(len(TEST_ACCOUNTS))

        print("Тест успешно завершен!")

    except Exception as e:
        pytest.fail(f"Тест не пройден: {str(e)}")
