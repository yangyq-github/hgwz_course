#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 18:11
# @File  : test_base.py
# __author__ = 'yangyanqin'
from Chapter_Ui_Auto.page.app import App

"""公用测试用例的封装"""
class TestBase:
    app = None

    def setup(self):
        self.app = App()
