from selenium.webdriver.common.by import By

from config import config


class InvestPage:
    # url = config.HOST + "/Index/index"

    invest_input_locator = (By.CSS_SELECTOR, ".form-control")
    confirm_invest_locator = (By.XPATH, '//button[contains(@class, "btn-special")]')

    def __init__(self, driver):
        self.driver = driver

    def send_keys_invest_input(self, money):
        """输入投标金额"""
        e = self.driver.find_element(*self.invest_input_locator)
        e.send_keys(money)
        return self

    def click_confirm_btn(self):
        """点击确认按钮"""
        e = self.driver.find_element(*self.confirm_invest_locator)
        # e.click()
        return e.text




