from selenium.webdriver.common.by import By

from common.base_page import BasePage


class UserPage(BasePage):

    # 查看余额
    money_locator = (By.XPATH, "//li[@class='color_sub']")

    def get_money(self):
        """获取用户余额"""
        e = self.driver.find_element(*self.money_locator)
        return e.text[:-1]