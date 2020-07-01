"""测试登录功能"""

import unittest
from selenium import webdriver
from config import config


class TestLogin(unittest.TestCase):

    def test_login_empty_mobile(self):
        """测试手机号码为空"""
        #1：打开浏览器，输入登录页面地址写，
        # 2：定位用户名
        # 3，输入用户名
        # 4，定位密码
        # 5，输入密码
        # 6，提交
        # 7，定位错误信息，断言
        driver = webdriver.Chrome()
        driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
        url = "http://120.78.128.25:8765/Index/login.html"
        driver.get(url)
        # 定位用户
        username_elem = driver.find_element("name", "phone")
        username_elem.send_keys("")
        # 定位密码
        pwd_elem = driver.find_element("name", "password")
        pwd_elem.send_keys("")
        # 提交
        login_btn_elem = driver.find_element("xpath", '//button[contains(@class, "btn-special")]')
        login_btn_elem.click()
        #
        error_msg_elem = driver.find_element("xpath", '//div[@class="form-error-info"]')
        self.assertEqual("请输入手机号", error_msg_elem.text)
        self.assertTrue("请输入手机号" == error_msg_elem.text)

        ## 测试用例完善的地方。
        # 1， 数据没有分离, DDT, 接口有差别。
        # 2， url 地址配置文件
        # 3， 登录地址放到用例数据？？？
        # 4， 元素定位的方式（数据）封装到哪里？？
        # 5， 浏览器管理放到 setUp
        # 6,  登录操作需要进行封装（函数，类？？） PO 模式， PageObject
        #


