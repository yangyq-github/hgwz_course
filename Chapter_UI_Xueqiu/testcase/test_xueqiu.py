#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 14:42
# @File  : test_xueqiu.py
# __author__ = 'yangyanqin'
from Chapter_UI_Xueqiu.page.app import App


class TestXueqiu:
    def setup(self):
        self.app = App()

    def test_market(self):
        search = self.app.start().goto_main().goto_market().goto_search()
        search.search("阿里巴巴")
        assert search.is_choosen("阿里巴巴")
