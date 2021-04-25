#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:35
# @File  : market.py
# __author__ = 'yangyanqin'
from selenium.webdriver.common.by import By

from Chapter_UI_Xueqiu.page.base_page import BasePage
from Chapter_UI_Xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self.drvier)
