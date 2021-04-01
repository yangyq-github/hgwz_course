#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/26 18:37
# @File  : test_selenium_location.py
# __author__ = 'yangyanqin'

"""定位用法"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocation():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def teardown(self):
        # self.driver.quit()
        pass

    def test_location(self):
        # self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("霍格沃茨测试学院")
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()
