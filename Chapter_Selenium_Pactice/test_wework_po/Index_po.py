#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 10:53
# @File  : Index_po.py
# __author__ = 'yangyanqin'
from Chapter_Selenium_Pactice.test_wework_po.register_po import Register
from Chapter_Selenium_Pactice.test_wework_po.login_po import Login
from selenium import webdriver


class Index():
    """首页的 PO"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(2)  # 隐式等待

    def goto_register(self):
        """
        点击立即注册
        进入到注册的 PO
        :return:
        """
        self.driver.find_element_by_link_text("立即注册").click()
        return Register(self.driver)  # 返回实例

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录的 PO
        :return:
        """
        self.driver.find_element_by_link_text("企业登录").click()
        return Login(self.driver)
