#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 9:52
# @File  : base_page.py
# __author__ = 'yangyanqin'
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        return self._driver.find_element(locator, value)
