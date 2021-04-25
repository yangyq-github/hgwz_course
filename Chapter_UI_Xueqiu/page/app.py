#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:27
# @File  : app.py
# __author__ = 'yangyanqin'
from appium import webdriver

from Chapter_UI_Xueqiu.page.base_page import BasePage
from Chapter_UI_Xueqiu.page.main import MainPage


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        if self.drvier is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True
            # 初始化 driver
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        else:
            # self.driver.start_activity(self._package, self._activity)
            # launch_app() 这个方法不需要传入任何参数，会自动启动起来 DesireCapa 里面定位的 activtiy
            self.drvier.launch_app()

        self.driver.implicitly_wait(10)
        return self

    def goto_main(self):
        """进入首页"""
        return MainPage(self.driver)
