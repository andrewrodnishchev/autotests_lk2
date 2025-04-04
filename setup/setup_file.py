import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://office.setuplk.ru/Account/Login?returnUrl=%2FClientOrg")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("admin@ast.ru")
    page.get_by_role("textbox", name="Пароль").click()
    page.get_by_role("textbox", name="Пароль").fill("admin")
    page.get_by_role("button", name="Вход").click()
    page.get_by_role("link", name="Добавить организацию").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("тест андрей")
    page.get_by_role("insertion").first.click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Организации", exact=True).click()
    page.get_by_role("link", name="Добавить организацию").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("сервисная")
    page.get_by_role("insertion").first.click()
    page.get_by_role("insertion").nth(1).click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Организации", exact=True).click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Устройства").click()
    page.get_by_title("Добавить устройство").click()
    page.locator("#HID").click()
    page.locator("#HID").fill("141 233 475")
    page.get_by_role("insertion").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_title("Добавить устройство").click()
    page.locator("#HID").click()
    page.locator("#HID").fill("027 478 388")
    page.get_by_role("insertion").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_title("Добавить группу").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("тест")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Коллекции").click()
    page.get_by_title("Добавить коллекцию").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("по информации об устройстве")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_title("Действия").click()
    page.get_by_role("link", name="Изменить").click()
    page.get_by_role("link", name="Правила добавления устройств").click()
    page.get_by_role("link", name="").click()
    page.locator("#FiltrationType").select_option("ByDeviceInfo")
    page.locator("#Hid").click()
    page.locator("#Hid").fill("141*")
    page.get_by_label("ДОБАВЛЕНИЕ ПРАВИЛА").get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Коллекции устройств").click()
    page.get_by_title("Добавить коллекцию").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("по данным домена")
    page.get_by_role("button", name="Сохранить").click()
    page.locator("[id=\"-\\32 \"]").get_by_title("Действия").click()
    page.get_by_role("link", name="Изменить").click()
    page.get_by_role("link", name="Правила добавления устройств").click()
    page.get_by_role("link", name="").click()
    page.locator("#Server").click()
    page.locator("#Server").fill("dc01.test.local")
    page.locator("#Login").click()
    page.locator("#Login").fill("user1")
    page.locator("#Password").click()
    page.locator("#Password").fill("123")
    page.get_by_label("ДОБАВЛЕНИЕ ПРАВИЛА").get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Политики доступа").click()
    page.get_by_role("link", name="Добавить политику").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("разрешено")
    page.get_by_role("link", name="Правила доступа").click()
    page.locator(".iCheck-helper").first.click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Добавить политику").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("запрещено")
    page.get_by_role("link", name="Правила доступа").click()
    page.locator("div:nth-child(3) > .iradio_square-green > .iCheck-helper").first.click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Отделы").click()
    page.get_by_role("link", name="Добавить отдел").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("тестовый отдел")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Политики инвентаризации").click()
    page.get_by_role("link", name="Добавить политику").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("тест инвента")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name=" Администрирование ").click()
    page.get_by_role("link", name=" Виды лицензий").click()
    page.get_by_role("link", name="Создать").click()
    page.locator("#Title").click()
    page.locator("#Title").fill("соединение+чат")
    page.locator("#Title").click()
    page.locator("#Title").fill("соединение + чат")
    page.locator("#ChannelCount").click()
    page.locator("#ChannelCount").fill("1")
    page.locator("div:nth-child(3) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(4) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(5) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(6) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(7) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(8) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(9) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(10) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(11) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(12) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(13) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.locator("div:nth-child(15) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Создать").click()
    page.locator("#Title").click()
    page.locator("#Title").fill("без соединения")
    page.locator("#ChannelCount").click()
    page.locator("#ChannelCount").fill("1")
    page.locator(".iCheck-helper").first.click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name=" Лицензии").click()
    page.get_by_role("link", name="Создать").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Создать").click()
    page.locator("#TypeId").select_option("26")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name=" Учетные записи").click()
    page.get_by_role("link", name="Создать").click()
    page.locator("#Email").click()
    page.locator("#Email").fill("rodnischev@safib.ru")
    page.locator("#UserName").click()
    page.locator("#UserName").fill("Андрей Роднищев")
    page.locator("#Password").click()
    page.locator("#Password").fill("123")
    page.locator("#ConfirmPassword").click()
    page.locator("#ConfirmPassword").fill("123")
    page.get_by_role("insertion").nth(3).click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Создать").click()
    page.locator("#Email").click()
    page.locator("#Email").fill("andrey@mailforspam.com")
    page.locator("#UserName").click()
    page.locator("#UserName").fill("andrey")
    page.locator("#Password").click()
    page.locator("#Password").fill("123")
    page.locator("#ConfirmPassword").click()
    page.locator("#ConfirmPassword").fill("123")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name=" Мои организации ").click()
    page.get_by_role("link", name=" Организации").click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Сотрудники").click()
    page.get_by_role("link", name="Добавить сотрудника").click()
    page.locator("#EMail").click()
    page.locator("#EMail").fill("rodnischev@safib.ru")
    page.get_by_role("insertion").click()
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name="Сотрудники").click()
    page.get_by_role("link", name="Добавить сотрудника").click()
    page.locator("#EMail").click()
    page.locator("#EMail").fill("andrey@mailforspam.com")
    page.get_by_role("button", name="Сохранить").click()
    page.get_by_role("link", name=" Администрирование ").click()
    page.get_by_role("link", name=" Системные настройки").click()
    page.locator("#SMTPServer").click()
    page.locator("#SMTPServer").fill("mxz.safib.ru")
    page.locator("#SMTPPort").click()
    page.locator("#SMTPPort").fill("587")
    page.locator("#SMTPLogin").click()
    page.locator("#SMTPLogin").fill("test@safib.ru")
    page.locator("#SMTPPassword").click()
    page.locator("#SMTPPassword").fill("26PatHolPosAmo")
    page.locator("#ServiceEMail").click()
    page.locator("#ServiceEMail").fill("corp@safib.ru")
    page.locator("#TelegramApiId").click()
    page.locator("#TelegramApiId").fill("22979763")
    page.locator("#TelegramApiHash").click()
    page.locator("#TelegramApiHash").fill("ca5f6ae52503eaac4f693b7af94bcd85")
    page.locator("#TelegramPhoneNumber").click()
    page.locator("#TelegramPhoneNumber").fill("89202226365")
    page.get_by_role("button", name="Сохранить").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
