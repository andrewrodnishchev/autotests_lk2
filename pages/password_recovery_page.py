# pages/password_recovery_page.py

from playwright.sync_api import Page, expect
from PIL import Image, ImageFilter
import pytesseract
import io
import time
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_recovery_page(self):
        print("Переход на страницу восстановления пароля")
        self.page.click(PasswordRecoveryLocators.RECOVERY_LINK)
        self.page.wait_for_load_state("networkidle")

    def enter_email(self, email: str):
        print(f"Ввод email: {email}")
        self.page.fill(PasswordRecoveryLocators.EMAIL_INPUT, email)

    def solve_captcha(self) -> str:
        print("Распознавание капчи...")

    # Получаем оригинальное изображение
        captcha_element = self.page.locator(PasswordRecoveryLocators.CAPTCHA_IMAGE)
        screenshot_bytes = captcha_element.screenshot()

    # Увеличение размера и улучшение качества
        with Image.open(io.BytesIO(screenshot_bytes)) as image:
        # Увеличиваем размер в 2 раза с интерполяцией LANCZOS
            original_width, original_height = image.size
            enlarged_image = image.resize(
            (original_width * 1, original_height * 3),
                resample=Image.Resampling.BICUBIC
            )

        # Легкое шумоподавление
            enlarged_image = enlarged_image.filter(ImageFilter.SMOOTH)

        # Сохраняем для проверки
            enlarged_image.save("enlarged_captcha.png")

    # Конфигурация Tesseract для цифр
        custom_config = [
            r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789',  # Варианты конфигураций
            r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789',
            r'--oem 3 --psm 13 -c tessedit_char_whitelist=0123456789'
        ]

        return pytesseract.image_to_string(enlarged_image, config=custom_config).strip()

    def submit_recovery_form(self, captcha_text: str):
        print("Ввод капчи и отправка формы")
        self.page.fill(PasswordRecoveryLocators.CAPTCHA_INPUT, captcha_text)
        self.page.click(PasswordRecoveryLocators.RECOVER_BUTTON)

    def should_see_success(self):
        print("Проверка успешного восстановления")
        # Замените на актуальный локатор успешного сообщения
        expect(self.page.locator("text=Инструкции отправлены на ваш email")).to_be_visible()