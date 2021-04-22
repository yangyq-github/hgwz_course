#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/6 10:00
# @File  : test_appium_testcase_location.py
# __author__ = 'yangyanqin'
"""appium 用例录制
    测试用例的重要部分：
    第一：导入依赖--from appium import webdriver
    第二：capabilities 的设置---desire_cap 中的参数
    第三：初始化 driver
    第四：隐式等待，增强用例的稳定性
    第五：元素定位与操作：find+action
    第六：断言--assert
"""
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.webdriver import MobileBy


def test_appium_recording():
    # 利用 appium 来录制脚本
    desire_cap = {
        "platformName": "android",
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.xueqiu.android",
        "appActivity": ".view.WelcomeActivityAlias",
        "platformVersion": '6.0',
        "noReset": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
    driver.implicitly_wait(20)
    el0 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
    el0.click()
    el1 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    el1.click()
    el1.send_keys("alibaba")
    el2 = driver.find_element_by_xpath(
        "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
    el2.click()
    sleep(5)
    driver.quit()


def test_cappium_write_tests():
    #编写测试用例
    desire_cap = {
        "platformName": "android",
        "deviceName": "127.0.0.1:7555",
        "appPackage": "com.xueqiu.android",
        "appActivity": "com.xueqiu.android.common.MainActivity",
        "noReset": True,
        "dontStopAppOnReset": True,
        "skipDeviceInitializetion":True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
    driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
    driver.implicitly_wait(20)
    driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
    driver.find_element_by_xpath()
    driver.back()
    sleep(6)
