# config.py
import os

STANDS = {
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
        "base_url": "http://office.setup_lk.ru/Account/Login?returnUrl=%2F",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg",
        "license_key": ""
    }

}


def get_license_key():
    return STANDS[SELECTED_STAND]['license_key']


SELECTED_STAND = "corp"  # Значение по умолчанию


def get_stand_urls(stand: str) -> dict:
    return {
        "login_url": f"{STANDS[stand]['base_url']}{STANDS[stand]['login_path']}",
        "dashboard_url": f"{STANDS[stand]['base_url']}{STANDS[stand]['dashboard_path']}"
    }


# Остальные настройки
LOGIN = os.getenv("LOGIN", "rodnischev@safib.ru")
CORRECT_PASSWORD = os.getenv("CORRECT_PASSWORD", "1")
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN", "test@safib.ru")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "1")
INCORRECT_PASSWORD = os.getenv("INCORRECT_PASSWORD", "2")
DEFAULT_TIMEOUT = 10000
LONG_TIMEOUT = 60000  # 60 секунд для критичных операций
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
TEST_EMPLOYEE_EMAIL = "ast1@mailforspam.com"
