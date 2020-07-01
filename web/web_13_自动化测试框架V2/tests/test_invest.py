"""测试登录功能"""
import logging
import os
import unittest
import ddt
from selenium import webdriver
from config import config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from common.excel_handler import ExcelHandler
# from data.login_data import cases_error, cases_invalid, cases_success


cases_error = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_error")
cases_invalid = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_invalid")
cases_success = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_success")


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        """前置条件"""
        # 初始化浏览器
        # 访问被测试的网址
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
        self.driver.maximize_window()

        self.login_page = LoginPage(self.driver)
        self.login_page.get()


    def tearDown(self) -> None:
        """后置条件"""
        # 关闭浏览器
        self.driver.quit()

    @ddt.data(*cases_error)
    def test_login_empty_mobile(self, test_info):
        """测试手机号码为空"""
        self.login_page.login(test_info["mobile"], test_info["pwd"])
        # 获取实际结果
        error_msg = self.login_page.get_error_msg()
        # 断言
        try:
            self.assertEqual(test_info["expected"], error_msg)
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            raise e
    #
    @ddt.data(*cases_invalid)
    def test_login_invalid(self, test_info):
        self.login_page.login(test_info["mobile"], test_info["password"])
        # 获取实际结果
        error_msg = self.login_page.get_invalid_msg()
        # 断言
        try:
            self.assertEqual(test_info["expected"], error_msg)
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            raise e

    # 正向用例
    @ddt.data(*cases_success)
    def test_login_success(self, test_info):
        """登录成功"""
        # login_page = LoginPage(self.driver)
        self.login_page.login(test_info["mobile"], test_info["password"])

        #定位我的账户是不是页面逻辑？？
        # 应该放到 page 对象当中去，
        user_info = HomePage(self.driver).get_user_account()
        # 断言
        self.assertTrue(test_info["expected"] in user_info)


    # pytest 进行用例筛选非常灵活。



        ## 测试用例完善的地方。
        # 1， 数据没有分离, DDT, 接口有差别。
        # 2， url 地址配置文件
        # 3， 登录地址放到用例数据？？？
        # 4， 元素定位的方式（数据）封装到哪里？？
        # 6,  登录操作需要进行封装（函数，类？？） PO 模式， PageObject


        # 封装的方式：
        # 1， 测试用例方法更加简洁
        # 2， 登录方法可以重复使用
        # 3， 测试用例方法当中，有没有具体的页面逻辑？？实现了页面操作和测试的分离
        # 4， 当页面操作需要变化的时候，比如前段工程师修改了页面，提高了可维护性。
        # 5， 面试的时候经常会问的问题。
        # PO， 类的方式进行封装。


