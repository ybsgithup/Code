# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : homework_page.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from common.base_page import BasePage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Homework_page(BasePage):
    # 定位作业标签
    homework_locator = (By.XPATH, '//a[text()="作业"]')
    # 定位上传作业按钮
    up_homework = (By.XPATH, '//a[@class="sc-btn"]')

    # 点击作业标签
    def homework_click(self):
        # homework_elem = self.driver.find_element(*self.homework_locator)
        # homework_elem = self.driver.find_element(*self.homework_locator)
        # homework_elem.click()
        e = self.wait_element_clickable(self.homework_locator)
        e.click()

        time.sleep(3)

    # 点击上传作业按钮
    def up_homework_btn_clikc(self):
        up_homework_elem = self.driver.find_element(*self.up_homework)
        up_homework_elem.click()
        time.sleep(3)


