# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  @Time : 2020/07/13
  @Auth : 晨光
  @File : config.py
  @IDE  : PyCharm
  @Email: 624011110@qq.com
-------------------------------------------------
"""

import os


# 隐式等待的时间
IMPLICTLY_WAIT_TIMEOUT = 5


# host
HOST = 'https://www.ketangpai.com'



# root path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# excel_path
DATA_PATH = os.path.join(ROOT_PATH, 'data')


# image_path 保存截图的文件路径
IMG_PATH = os.path.join(ROOT_PATH, 'screenshot')