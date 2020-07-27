# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/13
  @Auth : 晨光
  @File : login_page.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from config import config


class LoginPage(BasePage):
    url = config.HOST + "/Home/User/login.html"

    # 存放所有的 locator
    # 用户名定位
    username_locator = (By.NAME, "account")
    # 密码元素定位
    pwd_locator = (By.NAME, "pass")
    # 登录按钮定位
    login_btn_locator = ("xpath", '//a[contains(@class, "btn-btn")]')



    def get(self):
        self.driver.get(self.url)
        return self

    def login(self, mobile, pwd):
        """登录操作"""
        # self.mobile_locator 查找用户名元素
        username_elem = self.driver.find_element(*self.username_locator)
        # 输入用户名
        username_elem.send_keys(mobile)
        # 定位密码
        pwd_elem = self.driver.find_element(*self.pwd_locator)
        # 输入密码
        pwd_elem.send_keys(pwd)
        # 提交
        login_btn_elem = self.driver.find_element(*self.login_btn_locator)
        login_btn_elem.click()
        time.sleep(5)
        return self

