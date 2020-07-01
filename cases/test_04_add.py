import json
import unittest

from libs import ddt
from scripts.handle_request import HandleRequest
from scripts.handle_excel import HandleExcel
from scripts.handle_yaml import do_yaml
from scripts.handle_log import do_log
from scripts.handle_mysql import HandleMysql
from scripts.handle_parameterize import Parameterize, GlobalData


@ddt.ddt
class TestAdd(unittest.TestCase):
    # 创建handleexcel对象
    do_excel = HandleExcel(do_yaml.get_data("excel", "filename"), "add")
    testcases_data = do_excel.read_data()   # 嵌套用例excel对象的列表

    @classmethod
    def setUpClass(cls):
        # 创建HandleRequest对象
        cls.do_request = HandleRequest()
        # 获取url版本请求头数据并添加至请求头中
        cls.do_request.add_headers(do_yaml.get_data("api", "api_version"))
        # 创建HandleMysql对象
        cls.do_mysql = HandleMysql()

        # 创建一个不存在的用户id，并加入到全局数据池中
        setattr(GlobalData, "${not_existed_id}", cls.do_mysql.get_not_existed_user_id())

        do_log.info("开始执行用例")

    @classmethod
    def tearDownClass(cls):
        cls.do_request.close()
        # 关闭连接
        cls.do_mysql.close()
        do_log.info("用例执行结束")

    @ddt.data(*testcases_data)
    def test_add(self, one_testcase):
        # 将excel中读取的请求参数进行参数化
        new_data = Parameterize.to_parma(one_testcase.data)
        # 拼接请求URL地址
        new_url = do_yaml.get_data("api", "base_url") + one_testcase.url

        # 进行加标
        res = self.do_request.send(one_testcase.method,
                                   new_url,
                                   json=new_data)

        # 获取响应数据并转化为字典类型
        actual_value = res.json()
        try:
            # 断言：预期结果==实际结果，断言结果
            self.assertEqual(one_testcase.expected_value,
                             actual_value.get("code"),
                             one_testcase.name)
        except AssertionError as e:
            # 此处使用日志器来记录日志！
            do_log.error(f"{one_testcase.name}：具体异常为{e}")
            # 把执行结果写入excel中“actual"和”result“
            self.do_excel.write_data(one_testcase, res.text, "失败")
            # 再次抛出异常
            raise e
        else:
            # if one_testcase.id == 2:
            # a.如果响应报文中含有token_info，说明当前用例为登录接口用例
            # b.从响应报文中获取token，然后添加至请求头中
            if "token_info" in res.text:
                token = res.json()["data"]["token_info"]["token"]
                # add_headers需要传字典类型
                # self.do_request.add_headers("Authorization", f"Bearer {token}")
                headers = {"Authorization": "Bearer " + token}
                self.do_request.add_headers(headers)

            self.do_excel.write_data(one_testcase, res.text, "成功")


if __name__ == '__main__':
    unittest.main()
