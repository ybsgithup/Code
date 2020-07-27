# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : test_03class.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from decimal import Decimal
import pytest
import time


# from data import data_success,data_not_course,data_lessthan_course,data_have_course
from data.class_data import my_learning_table
from pages.class_page import Class_details


class TestClass():
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", my_learning_table)
    def test_main_not_course(self,test_info, login):
        """进入班级"""
        # 先登录
        driver = login
        class_page = Class_details(driver)
        # 点击进入班级标签
        class_page.class_entrance_click()
        time.sleep(3)

        # 断言
        error_msg = class_page.get_my_learning_msg()
        assert test_info["expected"] == error_msg


