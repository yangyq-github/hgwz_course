#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 18:22
# @File  : test_selenium_alert.py
# __author__ = 'yangyanqin'
from Chapter_selenium.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep


class TestAlert(Base):
    def test_alert_baiduimg(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        # alert=Alert(self.driver).
        self.driver.find_element_by_id("stfile").send_keys(r"C:\Users\JS-Test-001\Pictures\Camera Roll\kyc.jpg")  # 上传文件
        sleep(10)
