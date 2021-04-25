#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:30
# @File  : main.py
# __author__ = 'yangyanqin'
from selenium.webdriver.common.by import By

from Chapter_UI_Xueqiu.page.base_page import BasePage
from Chapter_UI_Xueqiu.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        """进入行情页面"""
        # 伪造黑名单
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']").click()
        self.set_implicitly_wait(3)
        return Market(self.drvier)