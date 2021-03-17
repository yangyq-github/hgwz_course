#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/17 17:58
# @File  : test_allure_baidu.py
__author__ = 'yangyanqin'
"""百度搜索的案例"""
import allure,pytest,time,os
from selenium import webdriver

# 变量定义
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
driver_url=os.path.join(base_url,"uitl\chromedriver.exe")


@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data",[
    "pytest",
    "allure",
    "unittest"
])
class TestSearchBaidu():

    def test_steps_demo(self,test_data):
        with allure.step("打开百度首页"):
            driver=webdriver.Chrome(executable_path=driver_url)
            driver.get("https://www.baidu.com")
            driver.maximize_window()

        with allure.step(f"输入搜索词 {test_data}"):
            driver.find_element_by_name("wd").send_keys(test_data)
            time.sleep(2)
            driver.find_element_by_id("su").click()
            time.sleep(2)

        with allure.step("保存图片"):
            driver.save_screenshot("./baidu/b.png")
            allure.attach.file("./baidu/b.png",name=test_data,attachment_type=allure.attachment_type.PNG)

        with allure.step("关闭浏览器"):
            driver.quit()