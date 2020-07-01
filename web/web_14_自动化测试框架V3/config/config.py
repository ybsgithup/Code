"""配置。

yaml vs py ？？
- yaml, 通用的配置格式。 python, java, PHP, Go
- py, 在 python 项目中读取更方便。
"""

# 隐式等待的时间
import os

# 隐式等待的时间
IMPLICTLY_WAIT_TIMEOUT = 5

# host
HOST = 'http://120.78.128.25:8765'


# root path
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# excel_path
DATA_PATH = os.path.join(ROOT_PATH, 'data')


# TODO: 加显示等待定位 invalid 错误信息