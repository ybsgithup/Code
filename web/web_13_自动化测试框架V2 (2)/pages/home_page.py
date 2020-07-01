from config import config


class HomePage:
    url = config.HOST + "/Index/index"

    user_account_locator = ("xpath", "//a[@href='/Member/index.html']")
    invest_btn_locator = ("xpath", '//a[@class="btn btn-special"]')

    def __init__(self, driver):
        self.driver = driver

    def get_user_account(self):
        """获取用户的账号信息"""
        e = self.driver.find_element(*self.user_account_locator)
        return e.text

    def get(self):
        """访问首页"""
        self.driver.get(self.url)
        return self

    def click_invest_btn(self):
        """点击投标按钮"""
        e = self.driver.find_element(*self.invest_btn_locator)
        e.click()
        return self