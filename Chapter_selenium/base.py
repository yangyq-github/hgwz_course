#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 15:20
# @File  : base.py
# __author__ = 'yangyanqin'

from selenium import webdriver
import os


class Base():
    def setup(self):
        # selenium 多浏览器处理
        browser = os.getenv("chrome")  # 返回环境变量键的值(如果存在)，否则返回默认值。
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
