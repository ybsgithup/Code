import pytest
from selenium import webdriver

from config import config


@pytest.fixture()
def browser():
    """启动浏览器和关闭浏览器"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(config.IMPLICTLY_WAIT_TIMEOUT)
    driver.maximize_window()
    yield driver
    driver.quit()