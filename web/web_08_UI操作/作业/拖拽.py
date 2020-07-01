# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/22
  @Auth : 晨光
  @File : 拖拽.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

url = '  https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'


driver.get(url)

# 切换iframe
frame_elem = driver.find_element('xpath', '//iframe[@id="iframeResult"]')
driver.switch_to.frame(frame_elem)

# 定位元素
elem1 = driver.find_element('xpath', '//div[@id="draggable"]')
print(elem1)
elem2 = driver.find_element('xpath', '//div[@id="droppable"]')

# 方法一
ac = ActionChains(driver)
# ac.drag_and_drop(elem1,elem2)
# ac.perform()

# 方法二
ac.drag_and_drop_by_offset(elem1,265,10).perform()