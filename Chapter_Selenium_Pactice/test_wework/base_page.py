#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 17:23
# @File  : base_page.py
# __author__ = 'yangyanqin'
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9966"
            self._driver = webdriver.Chrome(options=option)
            self._driver.implicitly_wait(9)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        """
        :param by:定位方式
        :param locator: 元素
        :return:
        """
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        """
        :param by:定位方式
        :param locator: 元素
        :return:
        """
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator):
        """
        显式等待
        :param locator: 传递一个元组包括定位方式以及元素
        :return:
        """
        WebDriverWait(self._driver, 15).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        # 满足 condition 的显式等待
        WebDriverWait(self._driver, 15).until(condition)
