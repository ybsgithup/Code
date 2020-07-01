"""
PO模式， Page Object Model, 页面对象模型。
解释：
Page: 页面
Object: 对象
网页页面转化成了 python 的一个对象。
网页当中的流程操作，元素操作 ==》 对象当中的方法。
网页当中的名词，元素定位方式， ==》 python 对象的属性。

DOM

PO 带来的意义：
# 封装的方式：
# 1， 测试用例方法更加简洁
# 2， 登录方法可以重复使用
# 3， 测试用例方法当中，有没有具体的页面逻辑？？实现了页面操作和测试的分离
# 4， 当页面操作需要变化的时候，比如前段工程师修改了页面，提高了可维护性。
# 5， 面试的时候经常会问的问题。
# 6， 提高代码的可读性。
# PO， 类的方式进行封装。
"""
from config import config

class LoginPage:
    url = config.HOST + "/Index/login.html"

    def __init__(self, driver):
        self.driver = driver
        # self.url = config.HOST + "/Index/login.html"

    def get(self):
        """访问login页面"""
        self.driver.get(self.url)

    def login(self, mobile, pwd):
        """登录操作"""
        self.get()
        username_elem = self.driver.find_element("name", "phone")
        username_elem.send_keys(mobile)
        # 定位密码
        pwd_elem = self.driver.find_element("name", "password")
        pwd_elem.send_keys(pwd)
        # 提交
        login_btn_elem = self.driver.find_element("xpath", '//button[contains(@class, "btn-special")]')
        login_btn_elem.click()

    def get_error_msg(self):
        """获取错误信息"""
        e = self.driver.find_element("xpath", '//div[@class="form-error-info"]')
        return e.text

    def get_invalid_msg(self):
        e = self.driver.find_element("xpath", '//div[@class="layui-layer-content"]')
        return e.text
