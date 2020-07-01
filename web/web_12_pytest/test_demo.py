
import unittest

import pytest

@pytest.mark.demo
class TestDemo():
    # def __init__(self):
    #     pass

    @pytest.mark.linux
    @pytest.mark.success
    def test_demo(self):
        expected = "yuz"
        acutal = "yuz wang"
        assert expected not in acutal, "这次真的断言失败了，可能是因为元素的定位问题"

    def test_demo_success(self):
        pass


if __name__ == '__main__':
    pytest.main()
