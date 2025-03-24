from playwright.sync_api import Page, expect
from locators.protocol_locators import ProtocolLocators
from config.config import DEFAULT_TIMEOUT
import os

class ProtocolPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_protocols(self):
        """Переход в раздел протоколов"""
        self.page.click(ProtocolLocators.LOGS_MENU)
        self.page.click(ProtocolLocators.CONNECTION_PROTOCOLS)
        self.page.wait_for_load_state("networkidle")

    def open_protocol_details(self):
        """Открытие деталей протокола"""
        self.page.click(ProtocolLocators.BURGER_BUTTON)
        self.page.click(ProtocolLocators.OPEN_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def download_archive(self, download_dir: str):
        """Скачивание архива с проверкой"""
        # Устанавливаем директорию для загрузок
        self.page.context.set_default_timeout(DEFAULT_TIMEOUT*3)

        # Инициируем скачивание
        with self.page.expect_download() as download_info:
            self.page.click(ProtocolLocators.DOWNLOAD_BUTTON)

        download = download_info.value
        # Сохраняем файл в указанную директорию
        save_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(save_path)

        # Проверяем что файл скачался
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Файл не скачан: {save_path}")

        return save_path