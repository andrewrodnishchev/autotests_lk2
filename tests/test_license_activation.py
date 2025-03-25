import pytest
from pages.auth_page import AuthPage
from pages.profile_license_page import ProfileLicensePage
import config


def test_license_activation(page, stand):
    auth_page = AuthPage(page)
    license_page = ProfileLicensePage(page)
    TEST_LICENSE = "CB71353D-619BEC40-8076D68A-FF302886"

    try:
        auth_page.navigate_to_login_page()
        auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)
        license_page.navigate_to_profile()
        license_page.open_license_activation()
        license_page.activate_license(TEST_LICENSE)
    except Exception as e:
        page.screenshot(path=f"license_activation_error_{stand}.png")
        pytest.fail(f"Ошибка активации лицензии на стенде {stand}: {str(e)}")
