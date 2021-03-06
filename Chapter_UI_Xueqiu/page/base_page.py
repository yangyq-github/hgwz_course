#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/23 11:22
# @File  : base_page.py
# __author__ = 'yangyanqin'
import json


import yaml
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Chapter_UI_Xueqiu.page.handle_back import handle_black


class BasePage:
    _black_list = [
        (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
    ]
    _max_err_num = 3
    _error_num = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver



    def screenshot(self,path):
        # 截图
        self.driver.save_screenshot(path)

    @handle_black
    def find(self, by, locator=None):
        # 如果元素找到，就清空 error 计算
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    # def find(self, by, locator=None):
    #     """
    #     :param by:
    #     :param locator:传入元组
    #     :return:
    #     """
    #     try:
    #         # 如果元素找到，就清空 error 计算
    #         if locator is None:
    #             result = self.driver.find_element(*by)
    #         else:
    #             result = self.driver.find_element(by, locator)
    #         self._error_num = 0
    #         return result
    #     except Exception as e:
    #         # 如果没有找到，则进行黑名单处理
    #         if self._error_num > self._max_err_num:
    #             # 如果error次数大于指定值，清空 error 次数并抛出异常
    #             self._error_num = 0
    #             raise e
    #         self._error_num += 1
    #         for ele in self._black_list:
    #             # 对黑名单进行点击
    #             eles = self.finds(ele)
    #             if eles.__len__() > 0:
    #                 eles[0].click()
    #                 return self.find(by, locator)
    #         raise ValueError("元素不在黑名单中")

    def finds(self, by, locator=None):
        """
        :param by:
        :param locator:传入元组
        :return:
        """
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def set_implicitly_wait(self, second):
        """设置隐式等待"""
        self.driver.implicitly_wait(second)

    def steps_analysis_yaml(self, path, name):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)[name]
            # 对 yaml 文件中的参数做处理
            raw = json.dumps(steps)
            for key, value in self._params.items():
                # repr 把对象转换成 str
                raw = raw.replace('${' + key + '}', repr(value))
            steps = json.loads(raw)
            # 对 yaml 文件中的测试步骤进行判断
            for step in steps:
                if "action" in step.keys():
                    action = step["action"]
                    if "click" == action:
                        self.find(step["by"], step["locator"]).click()
                    if "send" == action:
                        self.find(step["by"], step["locator"]).send_keys(step["value"])
                    if "len > 0" == action:
                        eles = self.finds(step["by"], step["locator"])
                        return len(eles) > 0


    def back(self):
        self.driver.back()