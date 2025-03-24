import pytest
from pages.auth_page import AuthPage
from pages.profile_license_page import ProfileLicensePage
from config.config import LOGIN, CORRECT_PASSWORD

def test_license_activation(page):
    auth_page = AuthPage(page)
    license_page = ProfileLicensePage(page)
    TEST_LICENSE = "CB71353D-619BEC40-8076D68A-FF302886"

    try:
        # Авторизация
        page.goto("http://lk.corp.dev.ru/Account/Login")
        auth_page.login(LOGIN, CORRECT_PASSWORD)

        # Основные шаги
        license_page.navigate_to_profile()
        license_page.open_license_activation()
        license_page.activate_license(TEST_LICENSE)

    except Exception as e:
        page.screenshot(path="license_activation_error.png")
        pytest.fail(f"Ошибка активации лицензии: {str(e)}")