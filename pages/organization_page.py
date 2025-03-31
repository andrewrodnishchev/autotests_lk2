from playwright.sync_api import Page
from locators.organization_locators import OrganizationLocators
import config
import time


class OrganizationPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def create_organization(self, name: str):
        self.page.click(OrganizationLocators.ADD_ORGANIZATION_BUTTON)
        self.page.wait_for_load_state("networkidle")

        self.page.fill(OrganizationLocators.NAME_INPUT, name)
        self.page.click(OrganizationLocators.SAVE_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def delete_organization(self):
        # Ожидание и клик на кнопку Изменить
        self.page.wait_for_selector(OrganizationLocators.EDIT_BUTTON, state="visible", timeout=10000)
        self.page.click(OrganizationLocators.EDIT_BUTTON)

        # Ожидание и клик на кнопку Удалить организацию
        self.page.wait_for_selector(OrganizationLocators.DELETE_BUTTON, state="visible", timeout=10000)
        self.page.click(OrganizationLocators.DELETE_BUTTON)

        # Ожидание и подтверждение удаления
        self.page.wait_for_selector(OrganizationLocators.CONFIRM_DELETE_BUTTON, state="visible", timeout=10000)
        with self.page.expect_navigation():
            self.page.click(OrganizationLocators.CONFIRM_DELETE_BUTTON)

        # Проверка модального окна
        time.sleep(1)  # Небольшая задержка для стабилизации
        modal = self.page.locator(OrganizationLocators.SUCCESS_DELETE_MODAL)
        modal.wait_for(state="visible", timeout=10000)

        if not modal.is_visible():
            raise AssertionError("Модальное окно подтверждения удаления не появилось")
