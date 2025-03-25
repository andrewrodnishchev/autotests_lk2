# config.py

STANDS = {
    "linux": {
        "base_url": "http://lk.linux.safib.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg"
    },
    "dev": {
        "base_url": "http://lk.corp.dev.ru",
        "login_path": "/Account/Login",
        "dashboard_path": "/ClientOrg"
    }
}

# Добавляем недостающий атрибут
SELECTED_STAND = "dev"  # Значение по умолчанию


def get_stand_urls(stand: str) -> dict:
    return {
        "login_url": f"{STANDS[stand]['base_url']}{STANDS[stand]['login_path']}",
        "dashboard_url": f"{STANDS[stand]['base_url']}{STANDS[stand]['dashboard_path']}"
    }


# Остальные настройки
LOGIN = "rodnischev@safib.ru"
CORRECT_PASSWORD = "1"
ADMIN_LOGIN = "test@safib.ru"
ADMIN_PASSWORD = "1"
INCORRECT_PASSWORD = "2"
DEFAULT_TIMEOUT = 10000
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
