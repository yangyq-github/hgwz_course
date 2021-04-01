#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/31 10:58
# @File  : register_po.py
# __author__ = 'yangyanqin'
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class Register():
    """注册页面的 PO"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys("fdfaf")
        Industry_first = self.driver.find_element(By.CSS_SELECTOR, '.register_industry_maintype_item_link:nth-child(1)')
        Industry_first_ele = self.driver.find_element(By.CSS_SELECTOR,
                                                      '.js_register_industry_subtype_cnt:nth-child(1)>div:nth-child(1)')
        ActionChains(self.driver).click(self.driver.find_element_by_id("corp_industry")).click(Industry_first).click(
            Industry_first_ele).perform()
        time.sleep(3)

        return True
