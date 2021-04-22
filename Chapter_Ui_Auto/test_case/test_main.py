#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 10:04
# @File  : test_main.py
# __author__ = 'yangyanqin'
from Chapter_Ui_Auto.page.app import App


class TestMain():
    def test_main(self):
        app = App()
        app.start().main().goto_search()
