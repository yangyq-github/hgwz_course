#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 15:09
# @File  : test_add_member.py
# __author__ = 'yangyanqin'
from Chapter_Selenium_Pactice.test_wework.after_login_index import AfterLoginIndex

class TestAdd:
    def setup(self):
        self.addmemeber = AfterLoginIndex()

    def test_add(self):
        self.addmemeber.goto_add_member().add_member()
