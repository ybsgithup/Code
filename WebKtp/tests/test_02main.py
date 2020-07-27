# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/13
  @Auth : 晨光
  @File : test_02main.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from decimal import Decimal
import pytest
from data.main_data import data_success,data_not_course,data_lessthan_course,data_have_course
from pages.main_page import My_page


class TestMain():
    @pytest.mark.success
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("test_info", data_not_course)
    def test_main_not_course(self,test_info, login):
        """添加课程不存在 加入失败"""
        # 点击加入课程按钮
        driver = login
        main_page = My_page(driver)
        # 点击加入课程按钮
        main_page.join_course_btn_click()
        # 输入课程验证码
        main_page.security_code_input(test_info["security_code"])

        # 断言
        error_msg = main_page.get_not_course_mes()
        assert test_info["expected"] == error_msg

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", data_lessthan_course)
    def test_main_lessthan_course(self,test_info, login):
        """少于6位 加入失败"""
        # 点击加入课程按钮
        driver = login
        main_page = My_page(driver)
        # 点击加入课程按钮
        main_page.join_course_btn_click()
        # 输入课程验证码
        main_page.security_code_input(test_info["security_code"])

        # 断言
        error_msg = main_page.get_lessthan_course()
        assert test_info["expected"] == error_msg

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", data_success)
    def test_main_success(self,test_info, login):
        """加入成功"""
        # 点击加入课程按钮
        driver = login
        main_page = My_page(driver)
        # 点击加入课程按钮
        main_page.join_course_btn_click()
        # 输入课程验证码
        main_page.security_code_input(test_info["security_code"])

        # 断言
        error_msg = main_page.get_succeed_course_mes()
        assert test_info["expected"] == error_msg

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", data_have_course)
    def test_main_have_course(self,test_info, login):
        """加入课程已经存在"""
        # 先登录
        driver = login
        main_page = My_page(driver)
        # 点击加入课程按钮
        main_page.join_course_btn_click()
        # 输入课程验证码
        main_page.security_code_input(test_info["security_code"])

        # 断言
        error_msg = main_page.get_have_course_mes()
        assert test_info["expected"] == error_msg