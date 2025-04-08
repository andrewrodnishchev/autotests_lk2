import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://office.setuplk.ru/Account/Login?returnUrl=%2FClientOrg")
    page.get_by_role("row", name="Активен rodnischev@safib.ru").locator("i").click()
    page.get_by_role("link", name="Активировать лицензию").click()
    page.get_by_role("button", name="По умолчанию По умолчанию").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").dblclick()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="По умолчанию без соединения").click()
    page.get_by_role("button", name="Соединение только с разрешенными устройствами 2451688F-672EEA44-8F504E7B-").click()
    page.get_by_role("button", name="Соединение только с разрешенными устройствами 2451688F-672EEA44-8F504E7B-").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
