import pytest
from selenium import webdriver

from config import config
from data.login_data import cases_success
from pages.login_page import LoginPage


@pytest.fixture(scope="class")
def browser():
    """启动浏览器和关闭浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def refresh(browser):
    browser.refresh()
    yield
    print("没有后置")


@pytest.fixture()
def login(browser):
    # 调用 login_page 的 login() 函数
    # browser 代表的是 broser() 这个潜质条件的返回值，driver（浏览器对象）
    login_page = LoginPage(browser)
    # 传入正确的手机号码和密码
    user_info = cases_success[0]
    login_page.get().login(user_info["mobile"], user_info["password"])
    yield browser


