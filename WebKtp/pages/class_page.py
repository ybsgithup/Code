# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : class_page.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from common.base_page import BasePage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pages.main_page import My_page
# from pages.homework_page import Homework_page

class Class_details(BasePage):

    # 我的学习
    my_learning_locator = ("xpath", '//div[text()="我的学习"]')

    def class_entrance_click(self):
        """点击班级入口"""
        class_entrance_elem =self.driver.find_element(*My_page.entrance_class_locator)
        class_entrance_elem.click()
        time.sleep(6)
        # homework_elem = self.driver.find_element(*Homework_page.homework_locator)
        # homework_elem.click()


    def get_my_learning_msg(self):
        e = self.find(self.my_learning_locator)
        time.sleep(3)
        return e.text