import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://office.setuplk.ru/Account/Login?returnUrl=%2FClientOrg")
    page.get_by_role("link", name=" Мои организации ").click()
    page.get_by_role("link", name=" Мои организации ").click()
    page.get_by_role("link", name=" Организации").click()
    page.get_by_role("link", name="тест андрей").click()
    page.get_by_role("link", name="Политики инвентаризации").click()
    page.get_by_role("link", name="Добавить политику").click()
    page.locator("#Name").click()
    page.locator("#Name").fill("тест")
    page.get_by_role("button", name="Сохранить").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
