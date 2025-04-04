import pytest
import os
from pages.auth_page import AuthPage
from pages.protocol_page import ProtocolPage
import config


@pytest.fixture
def download_dir(tmp_path):
    dir_path = tmp_path / "downloads"
    dir_path.mkdir()
    return str(dir_path)


def test_protocol_download(page, stand, download_dir):
    auth_page = AuthPage(page)
    protocol_page = ProtocolPage(page)

    auth_page.navigate_to_login_page()
    auth_page.login(config.LOGIN, config.CORRECT_PASSWORD)

    try:
        protocol_page.navigate_to_protocols()
        protocol_page.open_protocol_details()

        downloaded_file = protocol_page.download_archive(download_dir)
        assert os.path.exists(downloaded_file), f"Файл не скачан: {downloaded_file}"
    except Exception as e:
        pytest.fail(f"Ошибка на стенде {stand}: {str(e)}")
