# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : handup_homework_page.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

from common.base_page import BasePage
from config import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from pywinauto import Desktop


class Handup_homework_page(BasePage):

    url = config.HOST + "/Course/homework/courseid/MDAwMDAwMDAwMLR2vd6Gz8mw.html"

    # 定位添加作业文件按钮
    # add_btn_locator = (By.XPATH, '//div[text()="添加作业文件"]')
    add_btn_locator = (By.XPATH, '//input[@name="file"]')
    # 提交按钮
    commit_btn_locator = ("xpath", '//a[text()="提交"]')
    # 已提交按钮
    already_commit_btn_locator = ("xpath", '//a[text()="已提交"]')
    # 更新提交按钮
    updata_commit_btn_locator = ("xpath", '//a[text()="更新提交"]')
    # 修改后更新提交按钮
    modify_updata_commit_btn_locator = ("xpath", '//a[contains(@class, "new-tj2")]')

    # 弹框确定按钮
    determine_btn_locator = ("xpath", '//a[text()="确定"]')
    # 作业更新提交成功提示信息
    updata_commit_msg_locator = ("xpath", '//div[text()="作业提交成功"]')
    # 知道了 按钮
    updata_commit_know_btn_locator = ("xpath", '//a[text()="知道了"]')
    # 作业留言
    homework_comment_locator = ("xpath", '//textarea[@id="comment"]')
    # 留言保存按钮
    comment_save_btn_locator = ("xpath", '//a[text()="保存"]')
    # 暂无留言
    none_comment__btn_locator = ("xpath", '//span[@class="s2"]')

    # 点击添加作业文件按钮
    def add_btn_commit(self):
        e = self.wait_element_clickable(self.commit_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 点击更新提交按钮
    def updata_commit_btn(self):
        e = self.wait_element_clickable(self.updata_commit_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 点击更新提交按钮
    def modify_updata_commit_btn(self):
        e = self.wait_element_clickable(self.modify_updata_commit_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 点击已提交按钮
    def already_commit_btn(self):
        e = self.wait_element_clickable(self.already_commit_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 弹框确定按钮
    def determine_btn(self):
        e = self.wait_element_clickable(self.determine_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 弹框知道了按钮
    def know_btn(self):
        e = self.wait_element_clickable(self.updata_commit_know_btn_locator)
        e.click()
        time.sleep(3)
        return self

    # 暂无留言按钮
    def none_comment__btn(self):
        e = self.wait_element_clickable(self.none_comment__btn_locator)
        e.click()
        time.sleep(5)
        return self

    # 更新提交成功返回信息
    def get_updata_success_msg(self):
        """获取按钮信息"""
        e = self.find(self.Join_course_btn_locator)
        return e.text




    # 添加作业文件按钮，并上传文件
    def add_btn_send(self,file):
        e = self.wait_element_clickable(self.add_btn_locator)
        time.sleep(3)
        e.send_keys(file)
        time.sleep(5)
        return self



    # 打开页面
    def get(self):
        self.driver.get(self.url)
        time.sleep(3)
        return self

    def get_succeed_commit_mes(self):
        """获取加入成功信息"""
        e = self.find(self.commit_btn_locator)
        return e.text

    # 留言并保存
    def homework_comment(self,comment):
        e = self.wait_element_clickable(self.homework_comment_locator)
        time.sleep(3)
        e.send_keys(comment)
        # 点击保存按钮
        e = self.wait_element_clickable(self.comment_save_btn_locator)
        e.click()
        time.sleep(5)
