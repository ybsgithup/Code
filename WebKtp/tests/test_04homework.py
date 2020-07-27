# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : test_04homework.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from decimal import Decimal
import pytest
from pages.homework_page import Homework_page

class TestHomework():
    @pytest.mark.success
    # @pytest.mark.parametrize("test_info", data_not_course)
    def test_up_homework_btn(self,in_class):
        """点击上传作业按钮"""
        driver = in_class
        homework_page = Homework_page(driver)
        # 点击作业标签
        homework_page.homework_click()
        # 点击上传作业按钮
        homework_page.up_homework_btn_clikc()
