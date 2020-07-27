# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/13
  @Auth : 晨光
  @File : test_01login.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
import logging
import os
import pytest
from selenium import webdriver
from config import config
# from pages.login_page import LoginPage
# from common.excel_handler import ExcelHandler
# from data.login_data import cases_error, cases_invalid, cases_success
from pages.main_page import My_page
from pages.login_page import LoginPage
from data.login_data import cases_success

class TestLogin():
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_login_success(self, test_info,browser):
        """登录成功"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])

        # 定位我的账户是不是页面逻辑？？
        # 应该放到 page 对象当中去，
        user_info = My_page(browser).get_Join_course_btn()
        # 断言
        assert test_info["expected"] in user_info
