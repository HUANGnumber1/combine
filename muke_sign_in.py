import re
from playwright.sync_api import Playwright, sync_playwright, expect


def muke_sign_in(playwright: Playwright) -> None:
    account = input("请输入账户号: ")
    password = input("请输入密码: ")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.icourse163.org/")
    page.get_by_role("button", name="登录/注册").click()
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.locator("#auto-id-1746708772405").click()
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.get_by_role("textbox", name="请输入手机号").click()
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.get_by_role("textbox", name="请输入手机号").fill(account)
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.get_by_role("textbox", name="请输入密码").click()
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.get_by_role("textbox", name="请输入密码").fill(password)
    page.locator("[id=\"x-URS-iframe1746708770238\\.3132\"]").content_frame.get_by_text("登 录").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    muke_sign_in(playwright)
