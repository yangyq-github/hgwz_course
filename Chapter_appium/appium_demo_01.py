#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/2 9:50
# @File  : appium_demo_01.py
# __author__ = 'yangyanqin'

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'com.android.settings.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.quit()
