#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 10:04
# @File  : test_main.py
# __author__ = 'yangyanqin'
from Chapter_Ui_Auto.page.app import App
from Chapter_Ui_Auto.test_case.test_base import TestBase


class TestMain(TestBase):

    def test_main(self):
        app = App()
        app.start().main().goto_search()

    def test_windows(self):
        # 通用测试用例的封装
        self.app.start().main().goto_search()
