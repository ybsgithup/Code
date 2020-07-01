# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/22
  @Auth : 晨光
  @File : 鼠标操作_高级搜索.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.maximize_window()

url = 'http://www.baidu.com'

driver.get(url)

# news_elem = driver.find_element('xpath' , '//a')

# 移动鼠标到设置上
ac = ActionChains(driver)
setting_elem = driver.find_element('id', 's-usersetting-top')
print(setting_elem)
# ac.context_click(setting_elem)   # 右击
ac.move_to_element(setting_elem)
ac.perform()

# 点击高级搜索
adv_setting_elem = driver.find_element('xpath', '//a[text()="高级搜索"]')
ac.click(adv_setting_elem)
ac.perform()

