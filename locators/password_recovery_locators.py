# locators/password_recovery_locators.py

class PasswordRecoveryLocators:
    RECOVERY_LINK = "xpath=/html/body/div[1]/div/div/div/form/div[3]/p/a"
    EMAIL_INPUT = "#Email"
    CAPTCHA_IMAGE = "#captcha"
    CAPTCHA_INPUT = "#CaptchaCode"
    RECOVER_BUTTON = "button:has-text('Восстановить доступ')"