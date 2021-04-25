#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:36
# @File  : search.py
# __author__ = 'yangyanqin'
from selenium.webdriver.common.by import By

from Chapter_UI_Xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,stock_name):
        """搜索功能"""
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("阿里巴巴")
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        self.find(By.XPATH,
                  f"//*[@text='{stock_name}' and @resource-id='com.xueqiu.android:id/stockName']/../..//*[@text='加自选']").click()

    def is_choosen(self,stock_name):
        eles = self.finds(By.XPATH,
                          f"//*[@text='{stock_name}' and @resource-id='com.xueqiu.android:id/stockName']/../..//*[@text='已添加']")
        return eles.__len__() > 0
