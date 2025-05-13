import re
import asyncio
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright
from sympy.codegen.fnodes import elemental
from sympy.printing.numpy import const


async def reading(page)->None:
      #使用page.locator定位具有指定class的元素
      element = page.locator('.xy_taskCard_bottom')
      # 在这个元素内部定位span元素并获取其文本内容
      spanText = await element.locator('span').text_content()
      print(spanText)

def run(playwright: Playwright) -> None:
      browser = playwright.chromium.launch(headless=False)
      context = browser.new_context()

      account = input("请输入账户号: ")
      password = input("请输入密码: ")

      page = context.new_page()
      page.goto("https://www.ai-augmented.com/")
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
      page.get_by_text("显示全部任务").click()
      element = page.locator('.xy_taskCard_bottom')
      #spanText = element.locator('span').text_content()
      for i in range(element.count()):#此处填入element的长度计算,len不能用
            spanText = element.nth(i).text_content()
            print(spanText)
      # reading(page)
      # ---------------------
      context.close()
      browser.close()


with sync_playwright() as playwright:
    run(playwright)

