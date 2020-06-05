import os

import yaml


class AnalysisData:
    def get_yaml_data(self, name):

        """
        返回yaml文件数据"
        :param name: 读取yaml文件的名字
        :return:
        """
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            # 解析数据
            return yaml.safe_load(f)

    def get_excel_data(self):
        """解析Excel"""
        pass

    def get_db_data(self):
        """解析数据库"""
        pass