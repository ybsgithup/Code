# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/21
  @Auth : 晨光
  @File : selenium基础操作.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from selenium import webdriver

driver = webdriver.Chrome()

url = 'http://www.baidu.com'

# 隐式等待 20m
driver.implicitly_wait(20)

# 1， 打开网页
driver.get(url)

# 2 ,   窗口最大化
driver.maximize_window()

# 3， 窗口最小化
driver.minimize_window()

# 4， 前进
driver.forward()

# 5， 后退
driver.back()

# 6， 刷新
driver.refresh()

# 7， 退出浏览器
driver.quit()

# 8， 关闭标签页
driver.close()