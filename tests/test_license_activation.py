import pytest

from conftest import setup_stand
from pages.auth_page import AuthPage
from pages.profile_license_page import ProfileLicensePage
import config


def test_license_activation(page, stand):
    auth_page = AuthPage(page)
    license_page = ProfileLicensePage(page)
    test_license = config.get_license_key(stand)  # Получаем ключ из конфига

    try:
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
        license_page.off_direct_control()
        license_page.navigate_to_profile()
        license_page.open_license_activation()
        license_page.activate_license(test_license)  # Используем полученный ключ
        license_page.on_direct_control()

    except Exception as e:
        pytest.fail(f"Ошибка активации лицензии на стенде {stand}: {str(e)}")
