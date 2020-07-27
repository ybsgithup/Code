# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/15
  @Auth : 晨光
  @File : test_06private_message.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from decimal import Decimal
import pytest
from data.private_message_data import private_message
from pages.private_message_page import Private_message_page

class TestPrivateMessage():
    @pytest.mark.success
    @pytest.mark.parametrize("test_info",private_message)
    def test_send_message_success(self,login,test_info):
        driver = login
        private_message_page = Private_message_page(driver)
        # 点击私信按钮
        private_message_page.private_message_btn_click()
        # 切换窗口
        driver.switch_to.window(driver.window_handles[-1])
        # 输入内容
        private_message_page.input_message(test_info["message"])
        # 点击发送按钮
        private_message_page.send_btn_click()




