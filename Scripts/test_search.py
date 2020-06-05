import os

import yaml

from Base.page import Page
from Base.driver import Driver
import pytest

def get_data():
    # 存储测试数据
    data_list = []
    # 打开文件
    with open('./Data' + os.sep + 'search.yml', 'r', encoding='utf-8')as f:
        # 解析数据
        data = yaml.safe_load(f)
        for i in data.values():
            data_list.append((i.get("input"), i.get("exp")))
        return data_list

class TestSearch:

    def setup_class(self):
        """点击搜索按钮"""
        Page.get_setting().click_search_btn()

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.mark.parametrize("search_text, search_exp", get_data())
    def test_search(self, search_text, search_exp):
        """
        搜索内容测试
        :param search_text: 搜索内容
        :param search_exp: 搜索预期结果
        :return:
        """
        # 搜索
        result = Page.get_search().get_search_result(search_text)
        # 断言
        assert search_exp in result
