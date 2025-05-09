import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    account = input("请输入账户号: ")
    password = input("请输入密码: ")

    page = context.new_page()
    page.goto("https://www.ai-augmented.com/")
    page.get_by_role("link", name="武汉理工大学").click()
    page.get_by_role("button", name="登录").click()
    page.get_by_role("tab", name="统一身份认证").click()
    page.get_by_role("button", name="登录").click()
    page.get_by_role("textbox", name="用户名").click()
    page.get_by_role("textbox", name="用户名").fill(account)
    page.get_by_role("textbox", name="密码").click()
    page.get_by_role("textbox", name="密码").fill(password)
    page.locator("#index_login_btn").click()
    page.get_by_role("button", name="继续登录").click()
    page.get_by_title("点击查看/刷新待完成学习任务").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)