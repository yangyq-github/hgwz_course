#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 11:45
# @File  : add_member.py
# __author__ = 'yangyanqin'
from time import sleep

from selenium.webdriver.common.by import By
from Chapter_Selenium_Pactice.test_wework.base_page import BasePage


class AddMember(BasePage):
    def add_member(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID, 'username').send_keys("test_05")
        self.find(By.ID, 'memberAdd_acctid').send_keys("test_05_yang")
        self.find(By.ID, "memberAdd_phone").send_keys("18523354788")
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
