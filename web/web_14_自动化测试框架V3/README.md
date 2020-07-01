## 框架项目使用说明书
## 接口自动化测试项目结构是怎样的？？

- 运行脚本， run.py
- README.md 框架如何使用
- common (框架当中的通用模块)，是不会因为项目改变而改变的。
  （requests, excel, logger, config_handler, mysql）
- config (存储的是配置文件 yaml)
- logs (记录log 文件)
- data (测试用例数据)
- reports(测试报告)
- libs (第三方的模块， )
- cases/ tests (所有的测试用例)

## 页面功能介绍
tests.test_login.py   ## 实现测试用例逻辑部分
data.login_data.py    ## 用例存储测试数据，一个html页面一个文件
conftest.py  ## 用于存储初始化条件，这个文件会自动运行，不需要导入
pages.login_page.py   ## 用于实现页面的操作代码，一个html页面一个文件
config.config.py     ## 设置配置文件，如URL、路径、等待时间
？？  config.base_page.py   ## 封装通用方法
run_test.py  ## 执行运行用例，并生成测试报告
pytest.ini    ## 定义Marker标签