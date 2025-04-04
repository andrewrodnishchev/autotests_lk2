from playwright.sync_api import Page, expect
from locators.device_locators import DeviceLocators
import config


class DevicesPage:
    def __init__(self, page: Page):
        self.page = page
        self.urls = config.get_stand_urls(config.SELECTED_STAND)

    def navigate_to_devices(self):
        self.page.goto(self.urls["dashboard_url"])
        print("Переход в раздел 'Мой ассистент'")
        self.page.click(DeviceLocators.MY_ASSISTANT_MENU)
        print("Переход в раздел 'Устройства'")
        self.page.click(DeviceLocators.DEVICES_MENU)

    def add_device(self, device_id: str):
        print("Нажатие на кнопку 'Добавить устройство'")
        self.page.click(DeviceLocators.ADD_DEVICE_BUTTON)
        print(f"Ввод идентификатора устройства: {device_id}")
        self.page.fill(DeviceLocators.DEVICE_ID_INPUT, device_id)
        print("Нажатие на кнопку 'Сохранить'")
        self.page.click(DeviceLocators.SAVE_DEVICE_BUTTON)
        self.page.click(DeviceLocators.SAVE_DEVICE_BUTTON)

    def edit_device_comment(self, comment: str):
        print("Поиск кнопки бургера для устройства")
        burger_button = self.page.locator(DeviceLocators.BURGER_BUTTON)
        burger_button.wait_for(state="visible", timeout=10000)
        print("Клик по кнопке бургера")
        burger_button.click()

        print("Нажатие на кнопку 'Изменить'")
        self.page.click(DeviceLocators.EDIT_BUTTON)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("div.layout-ajax-locker", state="hidden", timeout=10000)

        print(f"Ввод комментария: {comment}")
        self.page.fill(DeviceLocators.COMMENT_INPUT, comment)

        print("Ожидание появления кнопки 'Сохранить'...")
        save_button = self.page.locator(DeviceLocators.SAVE_DEVICE_BUTTON)
        save_button.wait_for(state="visible", timeout=10000)
        print("Кнопка 'Сохранить' найдена")

        print("Нажатие на кнопку 'Сохранить'")
        save_button.click(timeout=60000)

    def delete_device(self):
        print("Поиск кнопки бургера для устройства")
        burger_button = self.page.locator(DeviceLocators.BURGER_BUTTON)
        burger_button.wait_for(state="visible", timeout=10000)
        print("Клик по кнопке бургера")
        burger_button.click()
        print("Нажатие на кнопку 'Удалить'")
        self.page.click(DeviceLocators.DELETE_BUTTON)
        print("Подтверждение удаления")
        self.page.click(DeviceLocators.CONFIRM_DELETE_BUTTON)

    def should_see_success_add_message(self):
        success_msg = self.page.locator(DeviceLocators.SUCCESS_ADD_MSG)
        expect(success_msg).to_be_visible()

    def should_see_success_save_message(self):
        expect(self.page.locator(DeviceLocators.SUCCESS_SAVE_MSG)).to_be_visible()

    def should_see_success_delete_message(self):
        expect(self.page.locator(DeviceLocators.SUCCESS_DELETE_MSG)).to_be_visible()
