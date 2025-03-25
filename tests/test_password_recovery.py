# tests/test_password_recovery.py

import pytest
from pages.auth_page import AuthPage
from pages.password_recovery_page import PasswordRecoveryPage
import config


def test_password_recovery(page, stand):
    auth_page = AuthPage(page)
    recovery_page = PasswordRecoveryPage(page)

    recovery_page.navigate_to_recovery_page()
    recovery_page.enter_email(config.LOGIN)

    captcha_text = recovery_page.solve_captcha()
    recovery_page.submit_recovery_form(captcha_text)

    recovery_page.should_see_success()
