"""测试登录功能"""
import logging
import time
import unittest
import ddt
from selenium import webdriver
from web.web_11_自动化测试框架V1.config import config
from web.web_11_自动化测试框架V1.pages.home_page import HomePage
from web.web_11_自动化测试框架V1.pages.login_page import LoginPage
from web_11_自动化测试框架V1.common.handle_excel import HandleExcel


@ddt.ddt
class TestLogin(unittest.TestCase):

    # login_page: object

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
    do_excel = HandleExcel("../data/test_case.xlsx", "cases_error")
    testcases_data_error = do_excel.read_data()
    # print(testcases_data_error)

    @ddt.data(*testcases_data_error)
    def test_login_empty_mobile(self, test_info):
        """测试手机号码为空"""
        # self.login_page.login(test_info["mobile"], test_info["password"])
        if test_info.mobile == None:
            test_info.mobile = ""
        if test_info.password == None:
            test_info.password = ""
        self.login_page.login(str(test_info.mobile), str(test_info.password))
        # 获取实际结果
        error_msg = self.login_page.get_error_msg()
        # 断言
        try:
            # self.assertEqual(test_info["expected"], error_msg)
            self.assertEqual(test_info.expected, error_msg)
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            raise e

    do_excel = HandleExcel("../data/test_case.xlsx", "cases_invalid")
    testcases_data_invalid = do_excel.read_data()

    @ddt.data(*testcases_data_invalid)
    def test_login_invalid(self, test_info):
        self.login_page.login(str(test_info.mobile), str(test_info.password))
        # 获取实际结果
        time.sleep(3)
        error_msg = self.login_page.get_invalid_msg()
        print(error_msg)
        # 断言
        try:
            self.assertEqual(test_info.expected, error_msg)
            logging.info("测试用例通过")
        except AssertionError as e:
            logging.error(f"测试用例不通过:{e}")
            raise e

    do_excel = HandleExcel("../data/test_case.xlsx", "cases_success")
    testcases_data_success = do_excel.read_data()

    # 正向用例
    @ddt.data(*testcases_data_success)
    def test_login_success(self, test_info):
        """登录成功"""
        # login_page = LoginPage(self.driver)
        self.login_page.login(str(test_info.mobile), str(test_info.password))

        #定位我的账户是不是页面逻辑？？
        # 应该放到 page 对象当中去，
        user_info = HomePage(self.driver).get_user_account()
        # 断言
        self.assertTrue(test_info.expected in user_info)




