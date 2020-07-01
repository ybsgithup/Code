# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/22
  @Auth : 晨光
  @File : 键盘操作.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
import time

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

url = 'http://baidu.com'

driver.get(url)

e = driver.find_element('id', 'kw')

e.send_keys('火影忍者')

e.send_keys(Keys.ENTER)

time.sleep(5)

scroll_jscode = "window.scrollTo(0, document.body.scrollHeight);"
driver.execute_script(scroll_jscode)

time.sleep(5)
driver.quit()