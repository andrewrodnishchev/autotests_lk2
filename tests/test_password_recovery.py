# tests/test_password_recovery.py

import pytest
from pages.password_recovery_page import PasswordRecoveryPage
from locators.password_recovery_locators import PasswordRecoveryLocators
import pytesseract

def test_password_recovery(page):
    recovery_page = PasswordRecoveryPage(page)

    # Указываем путь к Tesseract (для Windows)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    try:
        # Переход на страницу восстановления
        page.goto("http://lk.corp.dev.ru/Account/Login?returnUrl=%2FClientOrg")

        # Явное ожидание элемента
        page.wait_for_selector(PasswordRecoveryLocators.RECOVERY_LINK, timeout=10000)
        recovery_page.navigate_to_recovery_page()

        # Проверяем переход на страницу восстановления
        page.wait_for_selector(PasswordRecoveryLocators.EMAIL_INPUT, timeout=10000)
        recovery_page.enter_email("rodnischev@safib.ru")

        # Делаем скриншот капчи для отладки
        page.locator(PasswordRecoveryLocators.CAPTCHA_IMAGE).screenshot(path="captcha.png")

        # Решение капчи
        captcha_text = recovery_page.solve_captcha()
        print(f"Распознанная капча: {captcha_text}")

        if not captcha_text:
            pytest.fail("Не удалось распознать капчу")

        # Ввод капчи
        page.fill(PasswordRecoveryLocators.CAPTCHA_INPUT, captcha_text)

        # Отправка формы
        page.click(PasswordRecoveryLocators.RECOVER_BUTTON)

        # Проверка успешного восстановления
        page.wait_for_selector("text=Инструкции отправлены на ваш email", timeout=15000)

    except Exception as e:
        # Делаем скриншот при ошибке
        page.screenshot(path="test_error.png")
        pytest.fail(f"Тест завершился с ошибкой: {str(e)}")