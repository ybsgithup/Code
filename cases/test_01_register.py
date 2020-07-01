import unittest
from libs import ddt
from scripts.handle_request import HandleRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_yaml import do_yaml
from scripts.handle_log import do_log
from scripts.handle_mysql import HandleMysql
from scripts.handle_parameterize import GlobalData, Parameterize


@ddt.ddt
class TestRegister(unittest.TestCase):
    # 创建handleexcel对象
    do_excel = HandleExcel(do_yaml.get_data("excel", "filename"), "register")
    testcases_data = do_excel.read_data()  # 嵌套用例excel对象的列表

    @classmethod
    def setUpClass(cls):
        # 构造请求参数
        cls.do_request = HandleRequest()    # 创建HandleRequest对象
        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))    # 添加请求头到公共请求头

        cls.do_mysql = HandleMysql()   # 创建HandleMysql对象
        # cls.do_mysql.create_not_existed_mobile()
        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        # 释放资源
        cls.do_request.close()
        cls.do_mysql.close()
        do_log.info("用例执行结束")

    @ddt.data(*testcases_data)
    def test_register(self, one_testcase):
        # 在每条用例执行之前，获取未注册的手机号码，然后更新全局数据池
        setattr(GlobalData, "${not_existed_tel}", self.do_mysql.create_not_existed_mobile())

        # 将excel中读取的请求参数进行参数化
        new_data = Parameterize.to_parma(one_testcase.data)
        # 拼接请求URL地址
        new_url = do_yaml.get_data("api", "base_url") + one_testcase.url
        # 发送接口请求方法
        res = self.do_request.send(one_testcase.method,
                                   new_url,
                                   json=new_data)
        # 获取接口返回数据中的code值
        real_code = res.json()["code"]
        # row = testcase_dict["id"] + 1
        # self.do_excel.write_data(row, 7, res.text)
        # name = testcase_dict["name"]
        try:
            # 断言：预期结果==实际结果，断言结果
            self.assertEqual(one_testcase.expected_value,
                             real_code,
                             one_testcase.name)
        except AssertionError as e:
            # print("此处需要使用日志器来记录日志！")
            # my_logger.error(f"{one_testcase.name}：具体异常为{e}")
            # 此处使用日志器来记录日志！
            do_log.error(f"{one_testcase.name}：具体异常为{e}")
            # print(f"具体异常为：{e}")
            # self.do_excel.write_data(row, 8, "失败")
            # 把执行结果写入excel中“actual"和”result“
            self.do_excel.write_data(one_testcase, res.text, "失败")
            raise e
        else:
            # self.do_excel.write_data(row, 8, "成功")
            # do_log.debug(res.text)
            # 把执行结果写入excel中“actual"和”result“
            self.do_excel.write_data(one_testcase, res.text, "成功")


if __name__ == '__main__':
    unittest.main()
