#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 11:12
# @File  : page_base.py
# __author__ = 'yangyanqin'
from selenium import webdriver


class PageBase():
    """浏览器初始化"""

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(2)  # 隐式等待
