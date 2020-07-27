

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_user_account(self):
        """获取用户的账号信息"""
        e = self.driver.find_element("xpath", "//a[@href='/Member/index.html']")
        return e.text