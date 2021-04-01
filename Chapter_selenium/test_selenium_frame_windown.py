#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 15:13
# @File  : test_selenium_frame_windown.py
# __author__ = 'yangyanqin'

"""网页 frame 与多窗口操作"""
from time import sleep
from Chapter_selenium.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import pytest


class TestFrame(Base):

    # 针对多窗口的操作
    @pytest.mark.skip
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        login_handle = self.driver.current_window_handle
        print(f"登录窗口句柄：{login_handle}")
        self.driver.find_element_by_link_text("立即注册").click()
        # 获取所有窗口的句柄
        all = self.driver.window_handles
        # 窗口切换
        self.driver.switch_to_window(all[-1])
        print("注册页面句柄:" + str(self.driver.current_window_handle))
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("nihao")
        sleep(3)
        # 关闭当前标签页面
        # self.driver.close()
        self.driver.switch_to_window(login_handle)
        print("切换页面后的句柄:" + str(self.driver.current_window_handle))
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        print("点击登录链接之后的句柄:" + str(self.driver.current_window_handle))
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("你好吗")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("34324")
        sleep(3)
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(3)

    # 针对fram的操作以及alert
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到目标frame
        self.driver.switch_to_frame("iframeResult")
        # self.driver.switch_to.frame("iframeResult")
        ele = self.driver.find_element_by_id("draggable")
        tar = self.driver.find_element_by_id("droppable")
        sleep(5)
        # 拖拽
        ActionChains(self.driver).drag_and_drop(ele, tar).perform()
        # 弹出框的处理
        # 确认弹窗：driver.switch_to.alert.accept()
        # 取消按钮：driver.switch_to.alert.dismiss()
        t = self.driver.switch_to_alert()
        t.accept()
        #切换到默认frame
        self.driver.switch_to.default_content()
        sleep(3)
        self.driver.find_element_by_id("submitBTN").click()
        sleep(5)
