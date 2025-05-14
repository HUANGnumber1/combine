from selenium import webdriver
import time

base_url = "https://www.imooc.com/user/newlogin"
driver = webdriver.Chrome()
driver.get(base_url)

# 账号密码方式登录慕课网
# 找出元素有多种方法，自己喜欢怎样用就怎样用
name_input = driver.find_element_by_name('email')  # 找到用户名的框框
pass_input = driver.find_element_by_name('password')  # 找到输入密码的框框
login_button = driver.find_element_by_xpath('//div[@class="rlf-group clearfix"]/input')  # 找到登录按钮

username = "12345678900"  # 这里换成自己的账号
password = "******"  ##这里换成自己的密码

name_input.clear()
name_input.send_keys(username)  # 填写账号
time.sleep(0.2)  # 休眠一下，模拟人工登录，不然可能被拦截
pass_input.clear()
pass_input.send_keys(password)  # 填写密码
time.sleep(0.2)
login_button.click()  # 点击登录
time.sleep(0.2)

print(driver.get_cookies())  # 打印cookies
time.sleep(2)
print(driver.title)  # 打印标题
# driver.close()   #关闭浏览器

