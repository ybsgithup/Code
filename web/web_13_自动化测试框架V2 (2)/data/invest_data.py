"""通过 3 个列表导入所有的 login 测试数据。

没有采用 Excel 测试数据存储。
能不能用 Excel??
可以，但是流程比较复杂。一个 sheet 存储所有的 login 测试数据还可以吗？？？

为什么 case 不通用了？？
因为测试步骤不一样。流程不一样。
"""

cases_error = [
    {"money": 1, "expected": "请输入10的整数倍"},
    # {"tag":"error", "mobile": "13711112222", "password": "", "expected": "请输入密码"},
]

cases_invalid = [
    {"mobile": "13711112222", "password": "12", "expected": "此账号没有经过授权，请联系管理员!"}
]

cases_success = [
    {"mobile": "18684720553", "password": "python", "expected": "我的帐户[python]"}
]