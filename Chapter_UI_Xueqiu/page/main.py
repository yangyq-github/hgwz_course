#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:30
# @File  : main.py
# __author__ = 'yangyanqin'
import yaml
from selenium.webdriver.common.by import By


from Chapter_UI_Xueqiu.page.base_page import BasePage
from Chapter_UI_Xueqiu.page.market import Market


class MainPage(BasePage):
    def goto_market(self):
        """进入行情页面"""
        # 伪造黑名单
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='行情']").click()
        # 测试步骤的数据驱动实现
        self.steps_analysis_yaml("../driver_yaml/main.yaml","goto_market")
        # with open("../driver_yaml/main.yaml", encoding='utf-8') as f:
        #     steps = yaml.safe_load(f)
        #
        #     for step in steps:
        #         if "action" in step.keys():
        #             action = step["action"]
        #             if "click" == action:
        #                 self.find(step["by"],step["locator"]).click()

        self.set_implicitly_wait(3)
        return Market(self.driver)
