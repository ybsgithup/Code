"""测试投资功能

投资功能的测试步骤：
1， 打开浏览器
2， 登录
3， 登录成功，挑选投资对象
4， 进入投标页面
5， 输入投标金额
6， 出现错误结果或者是投资成功
7， 如何断言投资成功？？ 查数据库？  金额对比，
before_money - invest_money = after_money

接口自动化测试 ==》 接口 ==》后端工程
web 自动化测试 ==》 网页  ==》 前端工程
没有接口，前端和后端是搅和在一起的。前端为主（前端数据也是从后端来的。）
"""
from decimal import Decimal

import pytest
from data.invest_data import cases_error, cases_success
from pages.home_page import HomePage
from pages.invest_page import InvestPage


@pytest.mark.invest
class TestInvest():

    @pytest.mark.parametrize("test_info", cases_error)
    def test_invest_error(self,test_info, login):
        """投资失败"""
        # 首页点击投标
        driver = login  #
        home_page = HomePage(driver)
        # 点击投标按钮
        invest_page = home_page.get().click_invest_btn()
        # 投标页面
        # invest_page = InvestPage(driver)
        invest_page.send_keys_invest_input(test_info["money"])
        # 点击投标按钮
        actual_result = invest_page.get_btn_text()
        assert actual_result == test_info["expected"]

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", cases_success)
    def test_invest_success(self, test_info, login):
        # 获取现在的余额
        driver = login
        # 投资
        home_page = HomePage(driver)
        invest_page = home_page.get().click_invest_btn()

        # 投标之前的余额
        money_before = invest_page.get_money_before()
        # 输入投标金额
        invest_page.send_keys_invest_input(test_info["money"])
        invest_page.click_confirm_btn()
        # 断言
        print(invest_page.get_success_msg())
        assert test_info["expected"] in invest_page.get_success_msg()
        # 投标成功
        user_page = invest_page.click_active_btn()
        # 获取投资之后的余额
        money_after = user_page.get_money()
        # 字符串和数字不能相加
        # 坑：浮点数运行会丢失精度。
        assert Decimal(money_after) + Decimal(str(test_info["money"])) == Decimal(money_before)





