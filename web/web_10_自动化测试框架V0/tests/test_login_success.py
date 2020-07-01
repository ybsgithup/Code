# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/06/23
  @Auth : 晨光
  @File : test_login_success.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
"""测试登录功能"""

import unittest
from selenium import webdriver
from config import config


class TestLogin(unittest.TestCase):

    def test_login_success(self):
        """登录成功"""
        #1：打开浏览器，输入登录页面地址写，
        # 2：定位用户名
        # 3，输入用户名
        # 4，定位密码
        # 5，输入密码
        # 6，提交
        # 7，定位错误信息，断言
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
        url = "http://120.78.128.25:8765/Index/login.html"
        driver.get(url)
        # 定位用户
        username_elem = driver.find_element("name", "phone")
        username_elem.send_keys("18684720553")
        # 定位密码
        pwd_elem = driver.find_element("name", "password")
        pwd_elem.send_keys("python")
        # 提交
        login_btn_elem = driver.find_element("xpath", '//button[contains(@class, "btn-special")]')
        login_btn_elem.click()
        #
        error_msg_elem = driver.find_element("xpath", '//a[@href="/Member/index.html"]')
        self.assertEqual("我的帐户[python]", error_msg_elem.text)
        # self.assertTrue("请输入手机号" == error_msg_elem.text)