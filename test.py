import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.get_by_role("textbox", name="安理会上中方不得不投弃权票").click()
    page.get_by_role("textbox", name="安理会上中方不得不投弃权票").fill("俄罗斯阅兵")
    page.get_by_role("textbox", name="安理会上中方不得不投弃权票").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
