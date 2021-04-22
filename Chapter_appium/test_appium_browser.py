#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/12 9:34
# @File  : test_appium_browser.py
# __author__ = 'yangyanqin'
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "platformVersion": "6.0",
            "browserName": "Browser",
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        seach_ele = (By.ID, "index-bn")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(seach_ele))
        self.driver.find_element(*seach_ele).click()
        sleep(5)
