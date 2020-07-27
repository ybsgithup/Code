# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/15
  @Auth : 晨光
  @File : private_message_page.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from common.base_page import BasePage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Private_message_page(BasePage):

    # 私信按钮定位
    private_message_btn_locator = (By.XPATH, '//a[@href="/Letter/index.html"]')
    # 私信输入框定位
    input_box_locator = (By.XPATH, '//textarea[@class="ps-container"]')
    # 发送按钮
    send_btn_locator = (By.XPATH, '//a[contains(@class,"btn-positive")]')
    # 附件
    enclosure_locator = (By.XPATH, '//input[@name= "file"]')

    # 点击私信按钮
    def private_message_btn_click(self):
        e = self.wait_element_clickable(self.private_message_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 输入内容
    def input_message(self,message):
        e = self.wait_element_clickable(self.input_box_locator)
        e.send_keys(message)
        return self

    # 点击发送按钮
    def send_btn_click(self):
        e = self.wait_element_clickable(self.send_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 添加附件
    def add_Enclosure_btn(self, file):
        e = self.wait_element_clickable(self.enclosure_locator)
        e.send_keys(file)
        time.sleep(3)


