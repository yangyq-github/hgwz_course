#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/25 16:28
# @File  : test_selenium_basic.py
# __author__ = 'yangyanqin'
import time

from selenium import webdriver


# case 1 访问

class TestHogwards():
    def setup(self):
        # 初始化浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)#隐式等待

    def teardown(self):
        self.driver.quit()

    def test_hogwards(self):
        # 打开浏览器
        self.driver.get("https://testerhome.com")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_class_name("team-name").click()
        self.driver.find_element_by_partial_link_text("测试基础")