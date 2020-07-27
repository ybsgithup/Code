"""测试登录功能"""
import logging
import os
import pytest
from selenium import webdriver
from config import config
from pages.home_page import HomePage
from pages.login_page import LoginPage
from common.excel_handler import ExcelHandler
from data.login_data import cases_error, cases_invalid, cases_success


# cases_error = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_error")
# cases_invalid = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_invalid")
# cases_success = ExcelHandler(os.path.join(config.DATA_PATH, 'cases.xlsx')).read_data("login_success")

# 下面的代码全部使用pytest框架实现
class TestLogin():
    # def setUp

    # 参数化数据，cases_error从data.login_data导入
    @pytest.mark.parametrize("test_info", cases_error)
    # test_info命名上面和下面要一致，browser是在conftest.py中定义的前置条件
    def test_login_empty_mobile(self, test_info, browser):
        """测试手机号码为空"""
        # 初始化login_page对象，这里使用browser是因为browser中定义了driver
        login_page = LoginPage(browser)
        # 这里实现了打开网页，元素定位等操作，元素定位已经在login（）中实现；这里的get()方法使用了链式调用
        login_page.get().login(test_info["mobile"], test_info["password"])
        # 获取实际结果，实际结果操作已经封装在login_page.get_error_msg()中
        error_msg = login_page.get_error_msg()
        # 断言
        try:
            assert test_info["expected"] == error_msg
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            # 再次抛出异常
            raise e
    #
    @pytest.mark.parametrize("test_info", cases_invalid)
    def test_login_invalid(self, test_info, browser):
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        # 获取实际结果
        error_msg = login_page.get_invalid_msg()
        # 断言
        try:
            assert test_info["expected"] == error_msg
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            raise e

    # 正向用例
    @pytest.mark.smoke
    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_login_success(self, test_info, browser):
        """登录成功"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])

        #定位我的账户是不是页面逻辑？？
        # 应该放到 page 对象当中去，
        user_info = HomePage(browser).get_user_account()
        # 断言
        assert test_info["expected"] in user_info

