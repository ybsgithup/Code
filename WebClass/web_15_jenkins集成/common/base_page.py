import logging
import os

from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config import config
from datetime import datetime


class BasePage:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def find(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            # 没有找到元素
            logging.error(f"元素定位失败：{err}")
            self.save_screenshot()
        else:
            return e

    def save_screenshot(self):
        """截屏"""
        # 获取路径
        img_path = config.IMG_PATH
        # 生成截图的文件名时间戳
        ts_str = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        file_name = os.path.join(img_path, ts_str + ".png")
        self.driver.save_screenshot(file_name)
        return self

    def find_and_red(self, locator):
        """定位元素并且标成红色.。 装饰器实现。"""
        try:
            e = self.driver.find_element(*locator)
            # js 指令改变该元素的背景色。 border
            js_code = "arguments[0].style.borderColor='red';"
            self.driver.execute_script(js_code, e)

        except Exception as err:
            logging.error(f"元素定位失败：{err}")
        else:
            return e

    def wait_element_clickable(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可以被点击"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.element_to_be_clickable(locator))
        except Exception as err:
            self.save_screenshot()
            logging.error(f"元素定位失败：{err}")
        else:
            return e

    def wait_element_visible(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素可见"""

        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.visibility_of_element_located(locator))
            return e
        except Exception as err:
            self.save_screenshot()
            logging.error(f"元素定位失败：{err}")

    def wait_element_present(self, locator, timeout=20, poll_frequency=0.2):
        """等待元素被加载"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        try:
            e = wait.until(expected_conditions.presence_of_element_located(locator))
            return e
        except Exception as err:
            logging.error(f"元素定位失败：{err}")

    def click_element(self, locator):
        """点击某个元素"""
        e = self.wait_element_clickable(locator)
        e.click()
        return self

    def double_click(self, locator):
        """双击某个元素"""
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.driver)
        ac.double_click(e).perform()
        return self

    def move_to(self, locator):
        """鼠标悬停"""
        e = self.wait_element_clickable(locator)
        ac = ActionChains(self.driver)
        ac.move_to_element(e).perform()
        return self

    # 鼠标拖拽
    # 右击

    # 窗口切换
    # iframe
    # 文件上传
    # 滑动和拖拽

    def switch_to_frame(self, e, wait=False):
        """iframe 切换"""
        if not wait:
            self.driver.switch_to.frame(e)
            return self

        wait = WebDriverWait(self.driver, 30)
        wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(e))
        return self

    def window_scroll(self, width=None, height=None):
        """
        JavaScript API, Only support css positioning
        Setting width and height of window scroll bar.
        """
        if width is None:
            width = "0"
        if height is None:
            height = "0"
        js = "window.scrollTo({w},{h});".format(w=width, h=height)
        self.driver.execute_script(js)
        return self


