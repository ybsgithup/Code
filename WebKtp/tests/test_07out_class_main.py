# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/17
  @Auth : 晨光
  @File : test_07out_class_main.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from decimal import Decimal
import pytest
from data.main_data import out_class_success, out_class_error
from pages.main_page import My_page


class TestOutClassMain():
    @pytest.mark.success
    # @pytest.mark.run(order=1)
    @pytest.mark.parametrize("test_info", out_class_error)
    def test_out_class_failed(self, test_info, login):
        """退课失败"""
        # 登录
        driver = login
        main_page = My_page(driver)

        # 点击更多按钮
        main_page.more_btn_click()
        # 点击退课标签按钮
        main_page.out_class_tabale_btn_click()
        # 输入验证码
        main_page.pwd_input(test_info["pwd"])
        # 点击退课按钮
        main_page.out_class_btn_click()


        # 断言
        error_msg = main_page.get_pwd_error()
        assert test_info["expected"] == error_msg

    # @pytest.mark.demo
    @pytest.mark.parametrize("test_info", out_class_success)
    def test_out_class_success(self,test_info, login):
        """退课成功"""
        # 登录
        driver = login
        main_page = My_page(driver)

        # 点击更多按钮
        main_page.more_btn_click()
        # 点击退课标签按钮
        main_page.out_class_tabale_btn_click()
        # 输入正确定密码
        main_page.pwd_input(test_info["pwd"])
        # 点击退课按钮
        main_page.out_class_btn_click()

    @pytest.mark.success
    # @pytest.mark.parametrize("test_info", out_class_error)
    def test_default_out_class(self, login):
        """取消退课"""
        driver = login
        main_page = My_page(driver)
        # 点击更多按钮
        main_page.more_btn_click()
        # 点击退课标签按钮
        main_page.out_class_tabale_btn_click()
        # 点击取消按钮
        main_page.default_btn_click()









