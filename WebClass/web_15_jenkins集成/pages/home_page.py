from common.base_page import BasePage
from config import config
from pages.invest_page import InvestPage


class HomePage(BasePage):
    url = config.HOST + "/Index/index"

    user_account_locator = ("xpath", "//a[@href='/Member/index.html']")
    invest_btn_locator = ("xpath", '//a[@class="btn btn-special"]')


    def get_user_account(self):
        """获取用户的账号信息"""
        e = self.find(self.user_account_locator)
        return e.text

    def get(self):
        """访问首页"""
        self.driver.get(self.url)
        return self

    def click_invest_btn(self):
        """点击投标按钮, 进入投标详情页"""
        # e = self.driver.find_element(*self.invest_btn_locator)
        e = self.find(self.invest_btn_locator)
        e.click()
        return InvestPage(self.driver)