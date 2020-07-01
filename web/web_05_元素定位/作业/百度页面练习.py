# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/20
  @Auth : 晨光
  @File : 百度页面练习.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""


# 定位页面 https://voice.baidu.com/act/newpneumonia/newpneumonia/

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/'

driver.get(url)
# 元素1
# e_baidu = driver.find_element('link text', '百度首页')
# e_baidu.click()

# 元素2
# e_qiehuandiqu = driver.find_element('xpath', '//span[text()="切换地区"]')
# e_qiehuandiqu.click()

# 元素3
# e_xianyouquezhen = driver.find_element('xpath', '//span[text()="现有确诊"]')
# e_xianyouquezhen.click()

# 元素4 没有这个元素

# 元素5
e_leiji = driver.find_element('xpath', '//label[@class="Virus_1-1-270_1KG-A3"]')
e_leiji.click()