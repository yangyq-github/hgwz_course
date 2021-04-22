#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/9 11:16
# @File  : test_appium_case_02.py
# __author__ = 'yangyanqin'
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import *
import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebPara:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.xueqiu.android",
            "appActivity": "com.xueqiu.android.common.MainActivity",
            "noReset": True,
            "dontStopAppOnReset": True,
            "skipDeviceInitializetion": True,
            "unicodeKeyboard": True,  # 输入中文时候需要设置unicodeKeyboard和resetKeyboard
            "resetKeyboard": True,
            "chromedriverExecutable": "C:\Program Files\Appium\\resources\\app\\node_modules\\appium\\node_modules\\appium-chromedriver\chromedriver\win\chromedriver"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        # self.driver.find_element_by_id("com.xueqiu.android:id/action_close").click()  # 取消按钮
        # self.driver.quit()
        pass

    @pytest.mark.parametrize('searchkey, type, price', [
        ("alibaba", "BABA", 2.8),
        ("xiaomi", "01810", 2.0)
    ])
    def test_search_para(self, searchkey, type, price):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name']").click()
        current_price = self.driver.find_element_by_xpath(
            f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        print(f"{searchkey}当前价格：{float(current_price.text)}")
        assert_that(float(current_price.text), close_to(float(current_price.text), price * 0.1))

    def test_hamcrest(self):
        # assert_that(10, equal_to(9), '这是一个提示')  # 等于
        # assert_that(13, close_to(10,3))  # 期望值在10-13之间，3是以10为基础的浮动值
        assert_that("1 2", contains_string("2"))  # 是否包含字符串

    def test_xueqiu_trade(self):
        # 点击交易
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='交易']").click()
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击 A股开户
        self.driver.find_element_by_accessibility_id("A股开户").click()
        print(self.driver.contexts)
        print(self.driver.page_source)

        # 原生应用需要转换到 纯web 页面
        phone_ele = (MobileBy.ID, "phone-number")
        WebDriverWait(self.driver, 40).until(expected_conditions.element_to_be_clickable(phone_ele))
        self.driver.find_element(*phone_ele).send_keys("15875546566")
        self.driver.find_element_by_accessibility_id("获取验证码").click()
        self.driver.find_element_by_id("code").send_keys("123456")
        self.driver.find_element_by_accessibility_id("立即开户").click()
        # sleep(5)
