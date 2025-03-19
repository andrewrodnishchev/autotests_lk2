# pages/message_page.py

from playwright.sync_api import Page, expect
from locators.message_locators import MessageLocators
from datetime import datetime

class MessagePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_organization_devices(self):
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(MessageLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Устройства'")
        self.page.click(MessageLocators.DEVICES_MENU)

    def select_checkboxes(self):
        print("Выбор общего чекбокса")
        main_checkbox = self.page.locator(MessageLocators.MAIN_CHECKBOX)
        main_checkbox.wait_for(state="visible", timeout=10000)  # Ожидание появления чекбокса
        main_checkbox.click()  # Явный клик на чекбокс
        print("Общий чекбокс выбран")

    def send_message_to_devices(self, message: str):
        print("Нажатие на кнопку 'Отправить сообщение'")
        self.page.click(MessageLocators.SEND_MESSAGE_BUTTON)

        # Генерация уникального сообщения с датой и временем
        full_message = f"{message} {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}"
        print(f"Ввод сообщения: {full_message}")
        self.page.fill(MessageLocators.MESSAGE_INPUT, full_message)

        print("Нажатие на кнопку 'Отправить'")
        self.page.click(MessageLocators.SEND_SUBMIT_BUTTON)

    def should_see_success_message(self):
        print("Проверка уведомления об успешной отправке")
        success_msg = self.page.locator(MessageLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()