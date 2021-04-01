#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 10:56
# @File  : login_po.py
# __author__ = 'yangyanqin'
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Chapter_Selenium_Pactice.test_wework_po.register_po import Register


class Login():
    """登录页面的 PO"""

    def __init__(self, driver: WebDriver):
        #WebDriver 注释，告诉编译器是什么类型的 driver
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        点击企业注册
        进入到注册的 PO
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
