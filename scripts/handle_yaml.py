import os
import yaml
from scripts.handle_path import CONF_FILE_PATH, CONF_PATH


class HandleYaml:

    def __init__(self, filename=None):
        if filename is None:
            # filename = "testcases.yaml"
            filename = CONF_FILE_PATH
        else:
            # 将配置文件名与路径进行拼接
            filename = os.path.join(CONF_PATH, filename)
        with open(filename, encoding="utf-8") as file:
            self.config_data = yaml.full_load(file)

    def get_data(self, section, option):
        """
        读取配置文件数据
        :param section: 区域名
        :param option: 选项名
        :return: 值
        """
        return self.config_data[section][option]


do_yaml = HandleYaml()

if __name__ == '__main__':
    do_yaml = HandleYaml()
    print(do_yaml.get_data("api", "api_version"))
