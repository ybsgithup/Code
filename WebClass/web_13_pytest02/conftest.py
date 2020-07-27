"""存储测试夹具，前置后置条件。
conftest.py 固定的文件，
好处：不需要导入。
"""

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def before_test_and_after():
    """启动浏览器"""
    print("正在启动浏览器")
    driver = webdriver.Chrome()

    yield driver  # 生成器，惰性求知。

    print("正在退出浏览器")
    driver.quit()