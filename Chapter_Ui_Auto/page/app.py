#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 9:54
# @File  : app.py
# __author__ = 'yangyanqin'
from appium.webdriver import webdriver

from Chapter_Ui_Auto.page.base_page import BasePage
from Chapter_Ui_Auto.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"

    def start(self):
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # 初始化 driver
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package,self._activity)

        self._driver.implicitly_wait(20)
        return self

    def main(self) -> Main:
        return Main(self._driver)
