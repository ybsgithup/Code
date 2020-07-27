# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : test_05handup_homework.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""
from decimal import Decimal
import pytest
from pages.handup_homework_page import Handup_homework_page
from pages.homework_page import Homework_page
from data.handup_homework_data import commit_success,homework_comment,updata_homework_success


class TestHomework():

    # @pytest.mark.demo
    @pytest.mark.parametrize("test_info", commit_success)
    def test_up_homework(self, in_homework, test_info):
        """上传作业文件并提交"""
        driver = in_homework
        handup_homework_page = Handup_homework_page(driver)
        # 点击并上传文件
        handup_homework_page.add_btn_send(test_info["file"])
        # 点击提交按钮
        handup_homework_page.add_btn_commit()


        #断言
        user_info = handup_homework_page.get().get_succeed_commit_mes()
        assert test_info["expected"] == user_info

    @pytest.mark.success
    @pytest.mark.parametrize("test_info", homework_comment)
    def test_updata_homework(self,in_class, test_info):
        """更新作业并提交"""
        driver = in_class
        homework_page = Homework_page(driver)
        # 点击作业标签
        homework_page.homework_click()

        handup_homework_page = Handup_homework_page(driver)
        # 点击已提交按钮
        handup_homework_page.already_commit_btn()
        # 点击更新提交按钮
        handup_homework_page.updata_commit_btn()
        # 弹框点击确认按钮
        handup_homework_page.determine_btn()
        # 点击留言按钮
        handup_homework_page.none_comment__btn()
        # 留言并保存
        handup_homework_page.homework_comment(test_info["comment"])
        # 点击更新提交按钮
        handup_homework_page.modify_updata_commit_btn()











