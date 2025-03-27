import pytest
from pages.auth_page import AuthPage
import config


@pytest.mark.regression
def test_unsuccessful_login(page, stand):
    auth_page = AuthPage(page)
    auth_page.navigate_to_login_page()

    # Запоминаем текущий URL перед попыткой входа
    initial_url = page.url

    # Пробуем войти с неверными данными
    auth_page.login(config.LOGIN, config.INCORRECT_PASSWORD)

    # Проверяем что авторизация НЕ прошла
    assert not auth_page.is_login_successful(), \
        "Ожидалось, что авторизация с неверным паролем не пройдет"

    # Проверяем что остались на той же странице
    assert page.url == initial_url, \
        "После неудачного входа URL должен остаться прежним"

    # Дополнительная проверка элементов страницы входа
    auth_page.should_remain_on_login_page()
