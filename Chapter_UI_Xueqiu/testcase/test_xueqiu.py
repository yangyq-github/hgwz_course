#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 14:42
# @File  : test_xueqiu.py
# __author__ = 'yangyanqin'
import pytest
import yaml
from Chapter_UI_Xueqiu.page.app import App


def load_data():
    with open("../data_yaml/stock_name.yaml",encoding="UTF-8") as f:
        data = yaml.safe_load(f)
    return data


class TestXueqiu:
    def setup(self):
        self.app = App()

    @pytest.mark.parametrize("stock_name", load_data())
    def test_market(self, stock_name):
        search = self.app.start().goto_main().goto_market().goto_search()
        search.search(stock_name)
        assert search.is_choosen(stock_name)

        # search.back()
