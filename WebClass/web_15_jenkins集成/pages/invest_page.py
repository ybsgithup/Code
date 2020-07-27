from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.base_page import BasePage
from config import config
from pages.user_page import UserPage


class InvestPage(BasePage):
    # url = config.HOST + "/Index/index"

    invest_input_locator = (By.CSS_SELECTOR, ".form-control")
    confirm_invest_locator = (By.XPATH, '//button[contains(@class, "btn-special")]')
    # 投标成功信息
    invest_success_msg_locator = (By.XPATH, "//div[@class='layui-layer-content']//div[contains(@class, 'capital_font1')]")
    # 查看并激活按钮
    active_btn_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")


    def send_keys_invest_input(self, money):
        """输入投标金额"""
        e = self.find(self.invest_input_locator)
        # e = self.driver.find_element(*self.invest_input_locator)
        e.send_keys(money)
        return self

    def get_money_before(self):
        """获取投标之前的余额"""
        e = self.driver.find_element(*self.invest_input_locator)
        return e.get_attribute("data-amount")

    def get_btn_text(self):
        """获取投标按钮信息"""
        e = self.driver.find_element(*self.confirm_invest_locator)
        # e.click()
        return e.text

    def click_confirm_btn(self):
        """点击投标, 必须要用就显示等待 clickable """
        e = self.wait_element_clickable(self.confirm_invest_locator)
        e.click()
        return self

    def get_success_msg(self):
        """获取投标成功的信息"""
        e = self.wait_element_visible(self.invest_success_msg_locator)
        return e.text

    def click_active_btn(self):
        """点击查看并激活"""
        e = self.wait_element_clickable(self.active_btn_locator)
        e.click()
        return UserPage(self.driver)






