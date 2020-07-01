# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/20
  @Auth : 晨光
  @File : demo_02_查找元素.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from selenium import webdriver

# 设置浏览器
driver = webdriver.Chrome()

# 设置url地址
url = "http://www.baidu.com"

# 打开网页
driver.get(url)

# 浏览器最大化
driver.maximize_window()


# 元素查找
# js document.get
# input_elem = driver.find_element_by_id('kw')
input_elem = driver.find_element('id', 'kw')

# 往输入框中输入内容
input_elem.send_keys('美食剧')
# input_elem.send_keys()

# 定位百度一下按钮
# baidu_button = driver.find_element_by_id('su')
baidu_button = driver.find_element('id', 'su')

# 点击
baidu_button.click()


# 打开网页
driver.get('http://douban.com')

# 后退
driver.back()

# 刷新
driver.refresh()

# 最小化窗口
driver.minimize_window()

# 获取打开页面的url地址
print(driver.current_url)

# 获取打开页面的标题
print(driver.title)

# 获取打开页面的原代码
print(driver.page_source)

# 关闭浏览器
driver.quit()



