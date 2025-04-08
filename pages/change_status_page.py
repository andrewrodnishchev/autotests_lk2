from playwright.sync_api import Page, expect
from locators.change_status_locators import ChangeStatusLocators
import time


class ChangeStatusPage:
    def __init__(self, page: Page):
        self.page = page

    def open_accounts_section(self):
        try:
            self.page.click(ChangeStatusLocators.ADMIN_MENU)
            self.page.click(ChangeStatusLocators.ACCOUNTS_MENU_ITEM)
        except Exception as e:
            raise RuntimeError(f"Не удалось открыть раздел: {str(e)}")

    def select_accounts(self, emails: list):
        try:
            for email in emails:
                print(f"Ищем чекбокс для: {email}")
                checkbox = self.page.locator(
                    ChangeStatusLocators.CHECKBOX_BY_EMAIL.format(email)
                )

                checkbox.wait_for(state="visible", timeout=10000)
                print(f"Чекбокс найден, кликаем...")

                checkbox.scroll_into_view_if_needed()
                checkbox.hover()
                checkbox.click(force=True)

                if not checkbox.is_checked():
                    print("Чекбокс не изменил состояние, пробуем еще раз")
                    checkbox.click(force=True)

                print(f"Чекбокс для {email} успешно выбран")

        except Exception as e:
            raise RuntimeError(f"Ошибка выбора {email}: {str(e)}")

    def change_status_to_blocked(self, count: int):
        try:
            # Нажимаем кнопку Изменить статус
            self.page.click(ChangeStatusLocators.CHANGE_STATUS_BUTTON)

            # Открываем выпадающий список
            self.page.click(ChangeStatusLocators.STATUS_DROPDOWN)

            # Выбираем "Заблокирован"
            self.page.click(ChangeStatusLocators.STATUS_BLOCKED)

            # Нажимаем "Выполнить"
            self.page.click(ChangeStatusLocators.EXECUTE_BUTTON)

            # Проверяем модальное окно
            modal = self.page.locator(ChangeStatusLocators.SUCCESS_MODAL)
            expect(modal).to_contain_text(f"Успешно изменены статусы нескольких учетных записей ({count} шт.)")

        except Exception as e:
            raise RuntimeError(f"Ошибка изменения статуса: {str(e)}")

    def revert_status_changes(self, count: int):
        try:
            # Снова нажимаем кнопку Изменить статус
            self.page.click(ChangeStatusLocators.CHANGE_STATUS_BUTTON)

            # Нажимаем "Выполнить" без изменения статуса
            self.page.click(ChangeStatusLocators.EXECUTE_BUTTON)

            # Проверяем модальное окно
            modal = self.page.locator(ChangeStatusLocators.SUCCESS_MODAL)
            expect(modal).to_contain_text(f"Успешно изменены статусы нескольких учетных записей ({count} шт.)")

        except Exception as e:
            raise RuntimeError(f"Ошибка отката изменений: {str(e)}")
