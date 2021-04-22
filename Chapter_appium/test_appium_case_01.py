#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/7 9:29
# @File  : test_appium_case_01.py
# __author__ = 'yangyanqin'
"""以雪球 APP 为例来练习"""
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy


class TestAppiumCase01():
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
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attr(self):
        """判断元素是否可见"""
        research_ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(research_ele.text)
        print(research_ele.location)
        print(research_ele.size)
        if research_ele.is_enabled() == True:
            research_ele.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            ali_ele = self.driver.find_element_by_xpath(
                "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # 获取元素属性，并判断是否可见
            ele_displayed = ali_ele.get_attribute("displayed")
            if ele_displayed == 'true':
                print(ele_displayed)
                print("搜索成功")

    def test_touch_action(self):
        """滑动"""
        action = TouchAction(self.driver)
        # *************方法一：用固定坐标的方式，该方法比较死板******************
        # relase 释放，perform 执行
        # action.press(x=587, y=1532).wait(200).move_to(x=547, y=711).release().perform()
        # *************方法二：以当面屏幕的尺寸来当作坐标的使用，比较灵活******************
        window_rect = self.driver.get_window_rect()  # 获取当前屏幕的尺寸
        width = window_rect['width']
        height = window_rect['height']
        action.press(x=int(width / 2), y=int(height * 4 / 5)).wait(200).move_to(x=int(width / 2), y=int(
            height * 1 / 5)).release().perform()

    def test_my_info(self):
        """uiautomator 定位"""
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("验证码快捷登录")').click()
        self.driver.find_element_by_id("com.xueqiu.android:id/register_phone_number").send_keys("15845546645")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/register_code_text")').click()
        # toast 控件 learn--start
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"验证码已发送")]').text)  # 通过 文本包含的方式
        print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)  # 通过 class定位方式
        # toast 控件 learn--end
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/register_code")').send_keys("1234")
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        # print(self.driver.page_source)

    def test_child_selector(self):
        """父子或者兄弟来定位"""
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票"))').click()

    def test_scroll(self):
        """滚动查找元素"""
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("推荐")').click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("7X24快讯").instance(0));').click()



if __name__ == '__main__':
    pytest.main()
