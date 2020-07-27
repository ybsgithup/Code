# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/20
  @Auth : 晨光
  @File : demo_02_元素定位.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(url="http://www.baidu.com")

driver.maximize_window()
driv
# 第一种：id定位
e_id = driver.find_element('id', 'kw')
e_id.send_keys('最新电影')


# 第二种：name定位
e_name = driver.find_element('name', 'wd')
e_name.clear()
e_name.send_keys('刘欢')

# 第三种：class_name 定位
e_class = driver.find_element('class name', 's_btn')
e_class.click()

# 第四种：link_text
e_text = driver.find_element('link text', '图片')
e_text.click()

# 第五种：partial_link_text
e_link = driver.find_element('partial link text', '高清')
e_link.click()

# 第六种：xpath
e_xpath = driver.find_element('xpath', '//input[@id="kw" and @name="word"]')
e_xpath.clear()
e_xpath.send_keys('高清动漫壁纸')


