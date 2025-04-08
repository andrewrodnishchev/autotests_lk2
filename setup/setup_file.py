import argparse
import re
import time  # Добавлен импорт модуля time
from playwright.sync_api import Playwright, sync_playwright, expect
import sys
from pathlib import Path

# Автоматически определяем корень проекта
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from config import STANDS, get_stand_urls


def run_setup(playwright: Playwright, stand: str) -> None:
    """Основная функция выполнения сетапа"""
    start_time = time.time()  # Засекаем время начала выполнения
    # Получаем URL для выбранного стенда
    urls = get_stand_urls(stand)

    # Инициализация браузера
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # 1. Авторизация в системе
        print(f"🔐 Авторизация на стенде {stand}...")
        page.goto(urls["login_url"])
        page.get_by_role("textbox", name="Email").fill("admin@ast.ru")
        page.get_by_role("textbox", name="Пароль").fill("admin")
        page.get_by_role("button", name="Вход").click()
        expect(page).to_have_url(re.compile(urls["dashboard_url"]))
        print("✅ Авторизация успешна")

        # 2. Настройка SMTP (опционально)
        print("\n✉️ Настройка почтовых параметров...")
        page.get_by_role("link", name=" Администрирование ").click()
        page.get_by_role("link", name=" Системные настройки").click()
        page.locator("#SMTPServer").fill("mxz.safib.ru")
        page.locator("#SMTPPort").fill("587")
        page.locator("#SMTPLogin").fill("test@safib.ru")
        page.locator("#SMTPPassword").fill("26PatHolPosAmo")
        page.locator("#ServiceEMail").fill("corp@safib.ru")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Почтовые параметры настроены")

        # Настройка пароля на 1 символ

        page.get_by_role("link", name=" Системные настройки").click()
        page.get_by_role("link", name="Безопасность").click()
        page.locator("#PasswordRequiredLength").click()
        page.locator("#PasswordRequiredLength").fill("1")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Пароль настроен")

        # 3. Создание групп устройств
        print("\n📱 Создание групп устройств...")
        page.get_by_role("link", name=" Мой ассистент ").click()
        page.get_by_role("link", name=" Устройства").first.click()
        page.get_by_role("link", name="Добавить группу").click()
        page.locator("#Name").click()
        page.locator("#Name").fill("тест 1")
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("link", name="Добавить группу").click()
        page.locator("#Name").click()
        page.locator("#Name").fill("тест 2")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Группы устройств созданы...")

        # 4. Создание организаций
        print("\n🏢 Создание организаций...")
        page.get_by_role("link", name=" Мои организации ").click()
        page.get_by_role("link", name=" Организации").click()
        # Первая организация
        page.get_by_role("link", name="Добавить организацию").click()
        page.locator("#Name").fill("тест андрей")
        page.get_by_role("insertion").first.click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Организация 'тест андрей' создана")

        # Вторая организация
        page.get_by_role("link", name="Организации", exact=True).click()
        page.get_by_role("link", name="Добавить организацию").click()
        page.locator("#Name").fill("сервисная")
        page.get_by_role("insertion").first.click()
        page.get_by_role("insertion").nth(1).click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Сервисная организация создана")

        # 5. Добавление устройств
        print("\n📱 Добавление устройств...")
        page.get_by_role("link", name="Организации", exact=True).click()
        page.get_by_role("link", name="тест андрей").click()
        page.get_by_role("link", name="Устройства").click()

        # Первое устройство
        page.get_by_title("Добавить устройство").click()
        page.locator("#HID").fill("014 917 927")
        page.get_by_role("insertion").click()
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Устройство 014 917 927 добавлено")

        # Второе устройство
        page.get_by_title("Добавить устройство").click()
        page.locator("#HID").fill("174 570 314")
        page.get_by_role("insertion").click()
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Устройство 174 570 314 добавлено")

        # 6. Создание группы устройств
        page.get_by_title("Добавить группу").click()
        page.locator("#Name").fill("тест")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Группа устройств 'тест' создана")

        # 7. Работа с коллекциями
        print("\n🗂 Настройка коллекций...")
        page.get_by_role("link", name="тест андрей").click()
        page.get_by_role("link", name="Коллекции").click()

        # Первая коллекция
        page.get_by_title("Добавить коллекцию").click()
        page.locator("#Name").fill("по информации об устройстве")
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_title("Действия").click()
        page.get_by_role("link", name="Изменить").click()
        page.get_by_role("link", name="Правила добавления устройств").click()
        page.get_by_role("link", name="").click()
        page.locator("#FiltrationType").select_option("ByDeviceInfo")
        page.locator("#Hid").fill("141*")
        page.get_by_label("ДОБАВЛЕНИЕ ПРАВИЛА").get_by_role("button", name="Сохранить").click()
        print("  → Коллекция 'по информации об устройстве' настроена")

        # Вторая коллекция
        page.get_by_role("link", name="Коллекции устройств").click()
        page.get_by_title("Добавить коллекцию").click()
        page.locator("#Name").fill("по данным домена")
        page.get_by_role("button", name="Сохранить").click()
        page.locator("[id=\"-\\32 \"]").get_by_title("Действия").click()
        page.get_by_role("link", name="Изменить").click()
        page.get_by_role("link", name="Правила добавления устройств").click()
        page.get_by_role("link", name="").click()
        page.locator("#Server").fill("dc01.test.local")
        page.locator("#Login").fill("user1")
        page.locator("#Password").fill("123")
        page.get_by_label("ДОБАВЛЕНИЕ ПРАВИЛА").get_by_role("button", name="Сохранить").click()
        print("  → Коллекция 'по данным домена' настроена")

        # 8. Настройка политик доступа
        print("\n🛡 Настройка политик...")
        page.get_by_role("link", name="тест андрей").click()
        page.get_by_role("link", name="Политики доступа").click()

        # Первая политика
        page.get_by_role("link", name="Добавить политику").click()
        page.locator("#Name").fill("разрешено")
        page.get_by_role("link", name="Правила доступа").click()
        page.locator(".iCheck-helper").first.click()
        page.get_by_role("button", name="Сохранить").click()

        # Вторая политика
        page.get_by_role("link", name="Добавить политику").click()
        page.locator("#Name").fill("запрещено")
        page.get_by_role("link", name="Правила доступа").click()
        page.locator("div:nth-child(3) > .iradio_square-green > .iCheck-helper").first.click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Политики доступа настроены")

        # 8. Настройка политик инвентаризации
        page.get_by_role("link", name="Политики инвентаризации").click()
        page.get_by_role("link", name="Добавить политику").click()
        page.locator("#Name").click()
        page.locator("#Name").fill("тест")
        page.get_by_role("button", name="Сохранить").click()

        # 9. Создание отдела
        page.get_by_role("link", name="Отделы").click()
        page.get_by_role("link", name="Добавить отдел").click()
        page.locator("#Name").fill("тестовый отдел")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Отдел 'тестовый отдел' создан")

        # 10. Настройка лицензий (админ часть)
        print("\n🔑 Настройка лицензий...")
        page.get_by_role("link", name=" Администрирование ").click()
        page.get_by_role("link", name=" Виды лицензий").click()

        # Первый вид лицензии
        page.get_by_role("link", name="Создать").click()
        page.locator("#Title").fill("Соединение + чат")
        page.locator("#ChannelCount").fill("1")
        for i in range(3, 16):
            if i != 14:  # Пропускаем 14-й чекбокс
                page.locator(
                    f"div:nth-child({i}) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
        page.get_by_role("button", name="Сохранить").click()

        # Второй вид лицензии
        page.get_by_role("link", name="Создать").click()
        page.locator("#Title").fill("Без соединения")
        page.locator("#ChannelCount").fill("1")
        page.locator(".iCheck-helper").first.click()
        page.get_by_role("button", name="Сохранить").click()

        # Третий вид лицензии
        page.get_by_role("link", name="Создать").click()
        page.locator("#Title").click()
        page.locator("#Title").fill("Соединение только с разрешенными устройствами")
        page.locator("#ChannelCount").click()
        page.locator("#ChannelCount").fill("1")
        page.locator("div:nth-child(2) > .col-sm-10 > .i-checks > .icheckbox_square-green > .iCheck-helper").click()
        page.get_by_role("button", name="Сохранить").click()
        print("  → Виды лицензий созданы")

        # Создание лицензий
        page.get_by_role("link", name=" Лицензии").click()
        page.get_by_role("link", name="Создать").click()
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("link", name="Создать").click()
        page.locator("#TypeId").select_option("26")
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("link", name="Создать").click()
        page.locator("#TypeId").select_option("28")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Лицензии созданы")

        # 11. Создание учетных записей
        print("\n👥 Создание учетных записей...")
        page.get_by_role("link", name=" Учетные записи").click()

        # Первая учетная запись
        page.get_by_role("link", name="Создать").click()
        page.locator("#Email").fill("rodnischev@safib.ru")
        page.locator("#UserName").fill("Андрей Роднищев")
        page.locator("#Password").fill("1")
        page.locator("#ConfirmPassword").fill("1")
        page.get_by_role("insertion").nth(3).click()
        page.get_by_role("button", name="Сохранить").click()

        # Вторая учетная запись
        page.get_by_role("link", name="Создать").click()
        page.locator("#Email").fill("andrey@mailforspam.com")
        page.locator("#UserName").fill("andrey")
        page.locator("#Password").fill("1")
        page.locator("#ConfirmPassword").fill("1")
        page.get_by_role("button", name="Сохранить").click()

        # Третья учетная запись
        page.get_by_role("link", name="Создать").click()
        page.locator("#Email").fill("ast1@mailforspam.com")
        page.locator("#UserName").fill("ast1")
        page.locator("#Password").fill("1")
        page.locator("#ConfirmPassword").fill("1")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Учетные записи созданы")

        # 12. Добавление сотрудников
        print("\n🧑‍💼 Добавление сотрудников...")
        page.get_by_role("link", name=" Мои организации ").click()
        page.get_by_role("link", name=" Организации").click()
        page.get_by_role("link", name="тест андрей").click()
        page.get_by_role("link", name="Сотрудники").click()

        # Первый сотрудник
        page.get_by_role("link", name="Добавить сотрудника").click()
        page.locator("#EMail").fill("rodnischev@safib.ru")
        page.get_by_role("insertion").click()
        page.get_by_role("button", name="Сохранить").click()
        page.get_by_role("link", name="Сотрудники").click()

        # Второй сотрудник
        page.get_by_role("link", name="Добавить сотрудника").click()
        page.locator("#EMail").fill("andrey@mailforspam.com")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Сотрудники добавлены")

        # 13. Смена почты
        print("\n✉️ Изменение почты администратора...")
        page.get_by_role("link", name=" Администрирование ").click()
        page.get_by_role("link", name=" Учетные записи").click()
        page.get_by_role("row", name="Активен admin@ast.ru").locator("i").click()
        page.get_by_role("link", name="Изменить").click()
        page.locator("#Email").click()
        page.locator("#Email").fill("test@safib.ru")
        page.locator("#Password").click()
        page.locator("#Password").fill("1")
        page.locator("#ConfirmPassword").click()
        page.locator("#ConfirmPassword").fill("1")
        page.get_by_role("button", name="Сохранить").click()
        print("  → Почта изменена")

        print("\n🎉 Сетап успешно завершен!")

    finally:
        context.close()
        browser.close()

        # Вычисляем и выводим время выполнения
        end_time = time.time()
        total_time = end_time - start_time
        minutes = int(total_time // 60)
        seconds = int(total_time % 60)
        print(f"\n⏱ Общее время выполнения сетапа: {minutes} мин {seconds} сек")


def main():
    """Точка входа скрипта"""
    parser = argparse.ArgumentParser(description='Настройка тестового стенда')
    parser.add_argument('--stand',
                        choices=STANDS.keys(),
                        default='corp',
                        help='Выбор стенда для настройки')
    parser.add_argument('--headless',
                        action='store_true',
                        help='Запуск в headless режиме')

    args = parser.parse_args()

    with sync_playwright() as playwright:
        run_setup(playwright, args.stand)


if __name__ == "__main__":
    main()
