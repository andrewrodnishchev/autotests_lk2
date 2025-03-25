from playwright.sync_api import Page, expect
from locators.protocol_locators import ProtocolLocators
import config
import os


class ProtocolPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_protocols(self):
        self.page.goto(self.urls["dashboard_url"])
        self.page.click(ProtocolLocators.LOGS_MENU)
        self.page.click(ProtocolLocators.CONNECTION_PROTOCOLS)
        self.page.wait_for_load_state("networkidle")

    def open_protocol_details(self):
        self.page.click(ProtocolLocators.BURGER_BUTTON)
        self.page.click(ProtocolLocators.OPEN_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def download_archive(self, download_dir: str):
        self.page.context.set_default_timeout(config.DEFAULT_TIMEOUT * 3)
        with self.page.expect_download() as download_info:
            self.page.click(ProtocolLocators.DOWNLOAD_BUTTON)
        download = download_info.value
        save_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(save_path)
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Файл не скачан: {save_path}")
        return save_path
