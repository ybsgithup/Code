# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/14
  @Auth : 晨光
  @File : main_data.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""


data_not_course = [
    {"security_code": "P69U@#", "expected": "该加课码不存在或者已经失效"}
]

data_lessthan_course = [
    {"security_code": "P69UV", "expected": "加课验证码必须是6位字符"}
]

data_success = [
    {"security_code": "P69UVV", "expected": "加入课堂成功"}
]

data_have_course = [
    {"security_code": "P69UVV", "expected": "你已经选过此课程"}
]

# 成功退课
out_class_success = [
    {"pwd": "cetetek2012"}
]

# 退课输入任意内容
out_class_error = [
    {"pwd": "cetetek111@","expected": "密码错误"}
]

