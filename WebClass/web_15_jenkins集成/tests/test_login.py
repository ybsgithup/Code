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


class TestLogin():
    # def setUp

    @pytest.mark.parametrize("test_info", cases_error)
    def test_login_empty_mobile(self, test_info, browser):
        """测试手机号码为空"""
        login_page = LoginPage(browser)
        login_page.get().login(test_info["mobile"], test_info["password"])
        error_msg = login_page.get_error_msg()
        # 断言
        try:
            assert test_info["expected"] == error_msg
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
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

