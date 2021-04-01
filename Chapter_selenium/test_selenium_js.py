#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 17:54
# @File  : test_selenium_js.py
# __author__ = 'yangyanqin'
from Chapter_selenium.base import Base
from time import sleep


class TestJs(Base):
    def test_js(self):
        self.driver.get("https://testerhome.com/")
        self.driver.execute_script("document.documentElement.scrollTop=10000")  # 滚动到浏览器底部
        self.driver.execute_script("document.documentElement.scrollTop=0")  # 滚动到浏览器的顶部
        # a = self.driver.execute_script("return document.getElementById('main-nav-menu').value")  # 返回
        # b = self.driver.execute_script("return document.title")
        c = self.driver.execute_script(
            "return document.getElementById('main-nav-menu').value;return document.title")  # 合并用法
        print(c)
        sleep(4)

    def test_time(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script('a= document.getElementById("train_date");a.removeAttribute("readonly")')
        sleep(3)
        self.driver.execute_script('a.value="2021-04-01"')
        sleep(3)
        print(self.driver.execute_script('return a.value'))