import pytest
import os

from locators.protocol_locators import ProtocolLocators
from pages.auth_page import AuthPage
from pages.protocol_page import ProtocolPage
from config.config import LOGIN, CORRECT_PASSWORD, DEFAULT_TIMEOUT

@pytest.fixture
def download_dir(tmp_path):
    """Фикстура для временной директории загрузок"""
    dir_path = tmp_path / "downloads"
    dir_path.mkdir()
    return str(dir_path)

def test_protocol_download(page, download_dir):
    auth_page = AuthPage(page)
    protocol_page = ProtocolPage(page)

    # Авторизация
    page.goto("http://lk.corp.dev.ru/Account/Login")
    auth_page.login(LOGIN, CORRECT_PASSWORD)

    try:
        # Основные шаги
        protocol_page.navigate_to_protocols()
        protocol_page.open_protocol_details()

        # Клик по вкладке "События"
        page.click(ProtocolLocators.EVENTS_TAB)
        page.wait_for_timeout(2000)  # Небольшая пауза для загрузки

        # Скачивание и проверка
        downloaded_file = protocol_page.download_archive(download_dir)
        assert os.path.exists(downloaded_file), f"Файл не скачан: {downloaded_file}"
        print(f"Файл успешно скачан: {downloaded_file}")

    except Exception as e:
        page.screenshot(path="download_error.png")
        pytest.fail(f"Ошибка теста: {str(e)}")