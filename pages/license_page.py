# pages/license_page.py

from playwright.sync_api import Page, expect
from locators.license_locators import LicenseLocators

class LicensePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_organization_devices(self):
        print("Переход в организацию 'Тест Андрей'")
        self.page.click(LicenseLocators.ORGANIZATION_MENU)
        print("Переход в раздел 'Устройства'")
        self.page.click(LicenseLocators.DEVICES_MENU)

    def select_device_checkbox(self):
        print("Выбор чекбокса устройства")
        checkbox = self.page.locator(LicenseLocators.DEVICE_CHECKBOX).first
        checkbox.wait_for(state="visible", timeout=10000)
        checkbox.click()

    def activate_license(self):
        print("Нажатие на кнопку 'Активировать лицензию'")
        self.page.click(LicenseLocators.ACTIVATE_LICENSE_BUTTON)

        print("Открытие выпадающего списка лицензий")
        self.page.click(LicenseLocators.LICENSE_DROPDOWN)

        print("Выбор лицензии 'тест андрей CB71353D-...'")
        license_option = self.page.locator(LicenseLocators.LICENSE_OPTION)
        license_option.wait_for(state="visible", timeout=10000)
        license_option.click()

    def confirm_activation(self):
        print("Нажатие на кнопку 'Активировать'")
        activate_button = self.page.locator(LicenseLocators.ACTIVATE_BUTTON)
        activate_button.wait_for(state="visible", timeout=10000)
        activate_button.click()

    def should_see_success_message(self):
        print("Проверка уведомления об успешной активации")
        success_msg = self.page.locator(LicenseLocators.SUCCESS_MESSAGE)
        success_msg.wait_for(state="visible", timeout=10000)
        expect(success_msg).to_be_visible()