from common.base_page import BasePage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# from pages.invest_page import InvestPage


class My_page(BasePage):
    # url = config.HOST + "/Main/index.html"


    # 验证码输入框
    course_input_locator = ("xpath", '//input[@placeholder="请输入课程加课验证码"]')
    # 登录密码输入框
    pwd_input_locator = ("xpath", '//input[@placeholder = "请输入登录密码验证"]')




    # 已经选课验证信息
    have_course_mes_locator = ("xpath", '//span[text()="你已经选过此课程"]')
    # 错误验证码信息
    not_course_mes_locator = ("xpath", '//span[text()="该加课码不存在或者已经失效"]')
    # 少于6位字符
    lessthan_course_mes_locator = ("xpath", '//span[text()="加课验证码必须是6位字符"]')
    # 加入成功
    succeed_course_mes_locator = ("xpath", '//span[text()="加入课堂成功"]')
    # 班级入口
    entrance_class_locator = ("xpath", '//a[contains(text(), "考核项目")]')
    # 退课密码错误提示框
    pwd_error_mes_locator = ("xpath", '//span[text()="密码错误"]')
    # 其他
    other_locator = ("xpath", '//span[text()="警告：此操作无法撤消"]')


    # 加入课程按钮
    Join_course_btn_locator = ("xpath", '//div[contains(@class, "ktcon1l")]')
    # 确定按钮
    confirm_btn_locator = ("xpath", '//a[text()="确定"]')
    # 加入按钮
    join_btn_locator = ("xpath", '//a[text()="加入"]')
    # 更多按钮
    more_btn_locator = ("xpath", '//span[text()="更多"]')
    # 退课标签按钮
    out_class_table_btn_locator = ("xpath", '//a[text()="退课"]')
    # 退课按钮
    out_class_btn_locator = ("xpath", '//a[contains(@class, "btn-positive")][text()="退课"]')
    # 取消按钮(父亲找儿子定位方式）
    default_btn_locator = ("xpath", '//li[@class="dli1"]/a[contains(@class, "btn-default")]')

    def join_course_btn_click(self):
        """加入课程操作"""
        # 查找加入课程按钮元素
        join_course_btn_elem = self.driver.find_element(*self.Join_course_btn_locator)
        join_course_btn_elem.click()
        return self

    def more_btn_click(self):
        """点击更多按钮"""
        # 查找更多按钮元素
        more_btn_elem = self.driver.find_element(*self.more_btn_locator)
        more_btn_elem.click()
        return self

    def out_class_tabale_btn_click(self):
        """点击退课标签按钮"""
        # 查找退课标签按钮元素
        out_class_btn_elem = self.wait_element_clickable(self.out_class_table_btn_locator)
        out_class_btn_elem.click()
        return self


    def out_class_btn_click(self):
        """点击退课按钮"""
        # 查找退课按钮元素
        out_class_btn_elem = self.wait_element_clickable(self.out_class_btn_locator)
        out_class_btn_elem.click()
        return self


    def default_btn_click(self):
        """点击取消按钮"""
        # 查找取消按钮元素
        default_btn_elem = self.driver.find_element(*self.default_btn_locator)
        default_btn_elem.click()
        return self

    def other_btn_click(self):
        """点击其他按钮"""
        # 查找其他按钮元素
        other_btn_elem = self.driver.find_element(*self.other_locator)
        other_btn_elem.click()
        time.sleep(2)
        return self

    def security_code_input(self,security_code):
        # 输入课程验证码
        course_input_elem = self.driver.find_element(*self.course_input_locator)
        course_input_elem.click()
        course_input_elem.send_keys(security_code)
        # course_input_elem.send_keys("123456")
        time.sleep(2)
        # 点击确认按钮
        # confirm_btn_elem = self.driver.find_element(*self.confirm_btn_locator)
        # # confirm_btn_elem.send_keys(Keys.ENTER)
        # confirm_btn_elem.click()
        # 点击加入按钮
        confirm_btn_elem = self.driver.find_element(*self.join_btn_locator)
        confirm_btn_elem.click()
        time.sleep(3)

    def pwd_input(self,pwd):
        # 输入课程验证码
        pwd_input_elem = self.driver.find_element(*self.pwd_input_locator)
        pwd_input_elem.click()
        pwd_input_elem.send_keys(pwd)
        # course_input_elem.send_keys("123456")
        time.sleep(2)

    def get_Join_course_btn(self):
        """获取按钮信息"""
        e = self.find(self.Join_course_btn_locator)
        return e.text

    def get_have_course_mes(self):
        """获取已存在课程信息"""
        e = self.find(self.have_course_mes_locator)
        return e.text

    def get_not_course_mes(self):
        """获取验证码信息错误"""
        e = self.find(self.not_course_mes_locator)
        return e.text

    def get_lessthan_course(self):
        """获取验证码少于6位"""
        e = self.find(self.lessthan_course_mes_locator)
        return e.text

    def get_pwd_error(self):
        """获取退课密码错误"""
        e = self.find(self.pwd_error_mes_locator)
        return e.text

    def get_succeed_course_mes(self):
        """获取加入成功信息"""
        # e = self.find(self.succeed_course_mes_locator)
        e = self.find_and_red(self.succeed_course_mes_locator)
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