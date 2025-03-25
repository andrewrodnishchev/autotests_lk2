# pages/password_recovery_page.py

from playwright.sync_api import Page, expect
from PIL import Image, ImageFilter
import pytesseract
import io
from locators.password_recovery_locators import PasswordRecoveryLocators
import config


class PasswordRecoveryPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_recovery_page(self):
        print("Переход на страницу восстановления пароля")
        self.page.goto(f"{self.urls['login_url']}/Account/ForgotPassword")
        self.page.wait_for_load_state("networkidle")

    def enter_email(self, email: str):
        print(f"Ввод email: {email}")
        self.page.fill(PasswordRecoveryLocators.EMAIL_INPUT, email)

    def solve_captcha(self) -> str:
        print("Распознавание капчи...")
        captcha_element = self.page.locator(PasswordRecoveryLocators.CAPTCHA_IMAGE)
        screenshot_bytes = captcha_element.screenshot()

        with Image.open(io.BytesIO(screenshot_bytes)) as image:
            original_width, original_height = image.size
            enlarged_image = image.resize(
                (original_width * 1, original_height * 3),
                resample=Image.Resampling.BICUBIC
            )
            enlarged_image = enlarged_image.filter(ImageFilter.SMOOTH)
            enlarged_image.save("enlarged_captcha.png")

        custom_config = [
            r'--oem 3 --psm 8 -c tessedit_char_whitelist=0123456789',
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
        expect(self.page.locator("text=Инструкции отправлены на ваш email")).to_be_visible()
