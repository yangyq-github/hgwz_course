#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 9:59
# @File  : main.py
# __author__ = 'yangyanqin'
from Chapter_Ui_Auto.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Main(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID, 'tv_search').click()
