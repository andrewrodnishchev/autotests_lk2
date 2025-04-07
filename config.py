# config.py
import os
from typing import Dict, Any, TypedDict

STANDS: Dict[str, Dict[str, Any]] = {
    "linux": {
        "base_url": "http://lk.linux.safib.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg",
        "license_key": "10855EE1-A57FA04B-837409D0-F374E5"
    },
    "corp": {
        "base_url": "http://lk.corp.dev.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg",
        "license_key": "CB71353D-619BEC40-8076D68A-FF302886"
    },
    "win": {
        "base_url": "http://lk.win.safib.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg",
        "license_key": "9DE121FD-9697B746-AA7E1984-48BF1C4A"
    },
    "setup": {
        "base_url": "http://office.setuplk.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg",
        "license_key": ""
    }
}

SELECTED_STAND = "corp"  # Значение по умолчанию


class ConfigError(Exception):
    """Кастомное исключение для ошибок конфигурации"""
    pass


def validate_stand(stand: str) -> None:
    """Проверяет существование стенда"""
    if stand not in STANDS:
        available = ", ".join(STANDS.keys())
        raise ConfigError(f"Invalid stand: {stand}. Available stands: {available}")


def get_stand_urls(stand: str) -> Dict[str, str]:
    """Возвращает полные URL для указанного стенда"""
    validate_stand(stand)
    base = STANDS[stand]['base_url']
    return {
        "login_url": f"{base}{STANDS[stand]['login_path']}",
        "dashboard_url": f"{base}{STANDS[stand]['dashboard_path']}"
    }


def get_license_key(stand: str) -> str:
    """Возвращает лицензионный ключ для стенда"""
    validate_stand(stand)
    return STANDS[stand]['license_key']


# Остальные настройки
LOGIN = os.getenv("LOGIN", "rodnischev@safib.ru")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD", "1")
# ADMIN_LOGIN = os.getenv("ADMIN_LOGIN", "test@safib.ru")
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN", "admin@ast.ru")
# ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD", "2")
DEFAULT_TIMEOUT = 10000
LONG_TIMEOUT = 60000
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TEST_EMPLOYEE_EMAIL = "ast1@mailforspam.com"
