import unittest
import ddt
import pytest
from selenium import webdriver


# 如何定义 pytest 的前置条件
# 声明这是一个fixture 测试夹具，这是一个前置和后置条件



# def after_test(driver):
#
#     # 退出浏览器
#     driver.quit()


cases = [
    {"expected": 1},
    {"expected": 2},
    {"expected": 3}
]



class TestDemo():

    @pytest.mark.parametrize("case_info", cases)
    # @ddt.data(*cases)
    def test_demo(self, case_info, before_test_and_after):
        print("我正在进行测试")
        print("测试成功")
        self.assertTrue(case_info["expected"] == 3)

# if __name__ == '__main__':
#     pytest.main()


# class TestAdd:
#     @pytest.mark.parametrize("case_info", cases)
#     def test_add(self,case_info):
#         assert case_info["expected"] == 3




