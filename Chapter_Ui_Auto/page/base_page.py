#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/22 9:52
# @File  : base_page.py
# __author__ = 'yangyanqin'
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver
    _black_list = [(MobileBy.ID, '查询的元素')]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value):
        # 弹窗解决方案
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            # 处理完黑名单后，再次找原来的元素
            return self.find(locator, value)

    def steps(self, path):
        # 测试步骤的数据驱动
        with open(path) as f:
            steps = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    # 定位方式
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "click":
                        element.click()
