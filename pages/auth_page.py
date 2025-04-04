from playwright.sync_api import Page, expect
from locators.auth_page_locators import AuthPageLocators
import config
import time


class AuthPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)
        self.login_url = self.urls["login_url"]
        self.dashboard_url = self.urls["dashboard_url"]

    def navigate_to_login_page(self):
        self.page.goto(self.login_url)
        # Явно ждем загрузки страницы входа
        expect(self.page.locator(AuthPageLocators.LOGIN_BUTTON)).to_be_visible()

    def login(self, username: str, password: str):
        self.page.fill(AuthPageLocators.LOGIN_FIELD, username)
        self.page.fill(AuthPageLocators.PASSWORD_FIELD, password)
        self.page.click(AuthPageLocators.LOGIN_BUTTON)
        # Добавляем небольшую задержку для обработки запроса
        time.sleep(1)  # Лучше заменить на ожидание конкретного элемента

    def is_login_successful(self):
        """Проверяет успешную авторизацию по переходу на dashboard"""
        try:
            expect(self.page).to_have_url(self.dashboard_url, timeout=3000)
            return True
        except:
            return False

    def should_be_on_dashboard(self):
        expect(self.page).to_have_url(self.urls["dashboard_url"])

    def should_remain_on_login_page(self):
        """Проверяет, что после попытки входа остались на странице логина"""
        expect(self.page).to_have_url(self.login_url)
        # Дополнительная проверка, что кнопка входа все еще видна
        expect(self.page.locator(AuthPageLocators.LOGIN_BUTTON)).to_be_visible()

    # В auth_page.py можно добавить метод для получения токена
    def get_auth_token(self, username: str, password: str) -> str:
        self.page.on("request", lambda request: print(request.url, request.method))
        self.page.on("response", lambda response: print(response.url, response.status))

        self.login(username, password)

        # Или ищем конкретный запрос авторизации
        api_responses = []
    # В auth_page.py можно добавить метод для получения токена
