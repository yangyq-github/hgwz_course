#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 11:35
# @File  : test_register.py
# __author__ = 'yangyanqin'
from Chapter_Selenium_Pactice.test_wework_po.Index_po import Index


class TestRegister():

    def setup(self):
        self.index = Index()



    def test_register(self):
        result = self.index.goto_register().register()
        assert result
