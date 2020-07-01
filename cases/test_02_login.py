import unittest
import json

from libs import ddt
from scripts.handle_request import HandleRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_yaml import do_yaml
from scripts.handle_log import do_log
from scripts.handle_parameterize import Parameterize


@ddt.ddt
class TestLogin(unittest.TestCase):
    # 创建handleexcel对象
    do_excel = HandleExcel(do_yaml.get_data("excel", "filename"), "login")
    testcases_data = do_excel.read_data()  # 嵌套用例excel对象的列表

    @classmethod
    def setUpClass(cls):
        # 构造请求参数
        cls.do_request = HandleRequest()    # 创建HandleRequest对象

        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))  # 添加请求头到公共请求头
        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        # 释放资源
        cls.do_request.close()
        do_log.info("用例执行结束")

    @ddt.data(*testcases_data)
    def test_login(self, one_testcase):
        # 将excel中读取的请求参数进行参数化
        new_data = Parameterize.to_parma(one_testcase.data)
        # 拼接请求URL地址
        new_url = do_yaml.get_data("api", "base_url") + one_testcase.url
        # 发送接口请求方法
        res = self.do_request.send(one_testcase.method,
                                   new_url,
                                   json=new_data)

        # 获取响应数据并转化为字典类型
        actual_value = res.json()

        # 将expected_value期望值转化为字典类型
        expect_result = json.loads(one_testcase.expected_value, encoding='utf-8')
        try:
            # self.assertIn(one_testcase.expected_value,
            #               res.text,
            #               one_testcase.name)
            # 断言： 预期结果==实际结果，断言结果
            self.assertEqual(expect_result.get('code'), actual_value.get('code'), one_testcase.name)
            self.assertEqual(expect_result.get('msg'), actual_value.get('msg'), one_testcase.name)
        except AssertionError as e:
            # 此处使用日志器来记录日志！
            do_log.error(f"{one_testcase.name}：具体异常为{e}")
            # 把执行结果写入excel中“actual"和”result“
            self.do_excel.write_data(one_testcase, res.text, "失败")
            raise e
        else:
            # 把执行结果写入excel中“actual"和”result“
            self.do_excel.write_data(one_testcase, res.text, "成功")


if __name__ == '__main__':
    unittest.main()
