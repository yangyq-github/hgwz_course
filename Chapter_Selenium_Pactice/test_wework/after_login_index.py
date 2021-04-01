#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 11:42
# @File  : after_login_index.py
# __author__ = 'yangyanqin'
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Chapter_Selenium_Pactice.test_wework.add_member import AddMember
from Chapter_Selenium_Pactice.test_wework.base_page import BasePage


class AfterLoginIndex(BasePage):
    """登录成功之后的首页"""
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        """
        添加成员
        :return:
        """

        def add_memeber_condition(x):
            """
            改写显式等待条件
            :param x:
            :return:
            """
            elements_len = len(self.finds(By.ID, 'username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
                # 如果 username 不存在，就会触发 until 中的死循环
            return elements_len > 0


        self.find(By.ID, "menu_contacts").click()

        # ----------方法一 ------------
        time.sleep(4)
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        # 改造显式等待方法之前
        # ----------方法二 ------------
        # self.wait_for_click((By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)"))
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()

        # 改造显式等待方法之后
        # ----------方法三 ------------
        self.wait_for_condition(add_memeber_condition)

        return AddMember(self._driver)

    def goto_import_address(self):
        """
        导入通讯录
        :return:
        """
        pass

    def goto_join_member(self):
        """
        成员加入
        :return:
        """
        pass
