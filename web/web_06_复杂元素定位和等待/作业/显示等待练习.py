# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/21
  @Auth : 晨光
  @File : 显示等待练习.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

'''
1， 请指出强制等待，隐性等待和显性等待的区别。
强制等待：固定等待时间，不管元素是否提前加载完成，都需要等待固定的时间，
    且需要在每处需要添加等待的地方，单独添加等待命令行！
隐性等待：是全局的，只需要设置一次，所有元素都有固定的等待时间，如果在固定时间前加载完成，
    会提前结束等待时间。如果超出固定等待时间，就会报错，但隐式等待只能用来等待定位元素被加载，元素被发现。
显性等待：可以完成多种等待条件，如等待元素可见、等待元素可以被点击、等待窗口打开等等。只是显示等待实现步骤较前面两个，有点复杂。

'''

driver = webdriver.Chrome()

driver.implicitly_wait(30)

url = 'http://www.baidu.com'

driver.get(url)

# e = driver.find_element('id', 'kw')
# 等待输入框显示
wait = WebDriverWait(driver, timeout=5)
locator = ('id', 'kw')
e = wait.until(expected_conditions.visibility_of_element_located(locator))

# 输入柠檬班
e.send_keys('柠檬班')

# 等待百度一下按钮可以点击
wait = WebDriverWait(driver, timeout=5)
locator = ('id', 'su')
f = wait.until(expected_conditions.element_to_be_clickable(locator))

# 点击按钮
f.click()

# 等待元素加载完成
wait = WebDriverWait(driver,timeout=5)
locator = ('partial link text', '柠檬班腾讯课堂')
e = wait.until(expected_conditions.visibility_of_element_located(locator))

# 柠檬班腾讯课堂超连接
e.click()





