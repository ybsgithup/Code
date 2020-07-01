## web 自动化测试适用场景

测试金字塔？？
单元测试： 成本高， 不高？？ 效率 高？？

![image-20200525201513527](D:\data\雨泽\typora图片\image-20200525201513527.png)



什么样的项目适合做自动化测试？？

- 长期的。  

- 稳定。 中秋节搞活动，不适合！ api_v1, api_v2

- 规范的。  有文档，设计规范。 接口文档，需求文档。

- 重复的。 代码相关，代码适合做重复工作。

  访问不同的接口， 调用的函数， requests.post()



web 自动化测试 相比接口自动化测试。

web 自动化测试测试符合上述要求的功能 、场景。 主要是跑正向用例。



不是说 web 自动化测试没有用？





## web 自动化测试环境

- 浏览器 （谷歌浏览器）
- python 库： pip install selenium
- 浏览器的驱动：webdriver
  - 注意事项：webdriver 浏览的品牌要匹配
  - webdriver 版本要和浏览器兼容。不是说 81 的浏览器就一定要下载 81 的驱动。
  - 71，75,81,83以上的浏览器， 先下载 71的驱动试试。（71最稳定的版本，2.46有问题了，可以下载 71 的小版本。）
  - https://npm.taobao.org/mirrors/chromedriver/71.0.3578.80/，  群文件有 71 的 chromedriver
  - 镜像地址：https://npm.taobao.org/mirrors/chromedriver
  - 下载以后放到 python 安装根目录（环境变量）



## HTML 的构成

- 标签名称
- 标签属性
- 标签text文本内容
- 子标签

标签 ==》 元素

HTML 的构成：是 python 进行自动化测试的依据和基础，非常重要。

元素定位



## HTML 的各种元素

- html 标签
- a 
  - 和 href 属性
  - text 文本
- img
  - src
- iframe
  - 嵌套页面
- input 属性
  - 通常是和 name 属性搭配起来使用。
  - 文件：
  - value
- form 和 input 搭配

