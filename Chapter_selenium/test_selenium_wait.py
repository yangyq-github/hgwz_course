#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/26 10:20
# @File  : test_selenium_wait.py
# __author__ = 'yangyanqin'

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        # self.driver.implicitly_wait(2)#隐式等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()
        self.driver.find_element_by_link_text("所有分类").click()

        # time.sleep(2)
        def wait(x):
            return len(self.driver.find_elements(By.XPATH, '//*[@class="table-heading"]')) >= 1

        # WebDriverWait(self.driver, 10).until(wait)  # 显式等待
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))#元素是否可被点击，如果可被点击，则返回 元素，否则返回 false
        self.driver.find_element_by_link_text("开源项目").click()
