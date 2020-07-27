import pytest
from selenium import webdriver

from config import config
from data.login_data import cases_success
from pages.login_page import LoginPage
from pages.class_page import Class_details
from pages.homework_page import Homework_page
from selenium.webdriver import ChromeOptions

@pytest.fixture(scope="class")
# 设置浏览器前置条件
def browser():
    """启动浏览器和关闭浏览器"""
    chrome_options = ChromeOptions()
    chrome_options.binary_location = r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=chrome_options)
    # 初始化浏览器
    # driver = webdriver.Chrome()
    # 设置隐式等待
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    # 窗口最大化
    driver.maximize_window()
    # 返回driver，功能类似于return
    yield driver
    # yield 后面是后置条件
    # 所有代码执行完成后，关闭浏览器
    driver.quit()


@pytest.fixture()
# 前置条件，刷新页面，browser是为了使用driver
def refresh(browser):
    # 刷新页面，等同于driver.refresh()
    browser.refresh()

    yield
    print("没有后置")


@pytest.fixture()
# 操作课程的前置条件，登录操作
def login(browser):
    # 调用 login_page 的 login() 函数
    # browser 代表的是 browser() 这个前置条件的返回值，driver（浏览器对象）
    login_page = LoginPage(browser)
    # 传入正确的手机号码和密码
    user_info = cases_success[0]
    login_page.get().login(user_info["mobile"], user_info["password"])
    yield browser


@pytest.fixture()
# 进入作业页面的前置条件，先进入班级
def in_class(browser, login):
    # 调用 login_page 的 login() 函数
    # browser 代表的是 browser() 这个前置条件的返回值，driver（浏览器对象）
    # 先登录
    driver = browser
    class_page = Class_details(driver)
    # 点击进入班级标签
    class_page.class_entrance_click()

    yield browser

@pytest.fixture()
# 进提交作业的前置条件，先进入提交作业页面
def in_homework(browser, in_class):
    # 调用 login_page 的 login() 函数
    # browser 代表的是 browser() 这个前置条件的返回值，driver（浏览器对象）
    # 先登录
    driver = browser
    homework_page = Homework_page(driver)
    # 点击作业标签
    homework_page.homework_click()
    # 点击上传作业按钮
    homework_page.up_homework_btn_clikc()

    yield browser
