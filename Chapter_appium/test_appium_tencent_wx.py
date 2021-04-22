#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/20 14:58
# @File  : test_appium_tencent_wx.py
# __author__ = 'yangyanqin'
"""企业微信自动打卡"""
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# 加载yml数据
with open("./para_add.yml", encoding='UTF-8') as f:
    add_contracts = yaml.safe_load(f)


class TestTencentWx():
    def setup_class(self):
        # 每个类开始时候初始化 driver
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "platformVersion": '6.0',
            "skipServerInstallation": True,  # 跳过 uiautomator2 server的安装
            "skipDeviceInitialization": True,  # 跳过设备初始化
            "dontStopAppOnReset": True,  # 启动之前不停止app
            "settings[waitForIdleTimeout]": 0,
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown_class(self):
        # 释放 session
        self.driver.quit()

    """打卡功能"""

    def test_clock_in(self):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dy5' and @text='工作台']").click()
        # 滚动查找 "打卡" 元素
        # self.driver.find_element(
        #     MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
        #                                   '(new UiSelector().'
        #                                   'scrollable(true).'
        #                                   'instance(0)).'
        #                                   'scrollIntoView('
        #                                   'new UiSelector().'
        #                                   'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/els' and @text='打卡']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/guo' and @text='外出打卡']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/ap0']").click()
        result = self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/mr']").text
        assert '打卡成功' in result

    """添加联系人"""

    def test_add_contacts(self):
        name = "yang_001"
        gender = "男"
        phone = "18756456897"
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # 设置性别
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//../*[@text='男']").click()
        if gender == "男":
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        # 设置电话号码
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/eh_']//*[@text='手机号']").send_keys(
            phone)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()
        # 验证 toast
        result = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//*[@class='android.widget.Toast']")).text

        assert '添加成功' in result

    """参数化添加联系人"""

    @pytest.mark.parametrize('name,gender,phone', add_contracts)
    def test_para_add_contacts(self, name, gender, phone):
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='添加成员']").click()
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # 设置性别
        self.driver.find_element_by_xpath("//*[contains(@text,'性别')]/..//../*[@text='男']").click()
        if gender == "男":
            self.driver.find_element_by_xpath("//*[@text='男']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        # 设置电话号码
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/eh_']//*[@text='手机号']").send_keys(
            phone)
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("保存").instance(0));').click()
        # self.driver.find_element_by_xpath("//*[@text='保存']").click()
        # 验证 toast
        result = WebDriverWait(self.driver, 10).until(
            lambda x: x.find_element_by_xpath("//*[@class='android.widget.Toast']")).text

        assert '添加成功' in result
        self.driver.back()

    """删除联系人"""

    def test_delete_contacts(self):
        name = "yang_002"
        self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/dy5' and @text='通讯录']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/h8q").click()
        self.driver.find_element_by_id("com.tencent.wework:id/g1n").send_keys(name)
        sleep(2)
        eleslist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        if len(eleslist) < 2:
            print("未找到该联系人")
        else:
            #存在联系人，点击第一个
            eleslist[1].click()
            self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/h8g']").click()
            self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()
            self.driver.find_element(
                MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                              '(new UiSelector().'
                                              'scrollable(true).'
                                              'instance(0)).'
                                              'scrollIntoView('
                                              'new UiSelector().'
                                              'text("删除成员").instance(0));').click()
            self.driver.find_element_by_xpath("//*[@text='确定']").click()
            sleep(2)
            self.driver.back()
            eleslist = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
            if eleslist.__len__() == 1:
                print("删除成功")
