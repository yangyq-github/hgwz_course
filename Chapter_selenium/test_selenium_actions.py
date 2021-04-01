#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 9:24
# @File  : test_selenium_actions.py
# __author__ = 'yangyanqin'
"""web 控件的交互进阶"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions
import time, pytest
from Chapter_selenium.base import Base
from selenium.webdriver.common.keys import Keys


# PC端
@pytest.mark.skip
class TestActionChains(Base):
    # 鼠标点击
    def test_case_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        # 鼠标左键
        element_click = self.driver.find_element(By.XPATH, '//form//input[3]')
        # 鼠标双击
        element_double_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        # 鼠标右键
        element_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        # ActionChains(self.driver).move_to_element(element_click).click(element_click).perform()
        actions = ActionChains(self.driver)
        actions.click(element_click)
        actions.double_click(element_double_click)
        actions.context_click(element_right_click)
        # actions.click(actions)
        actions.perform()

    # 鼠标移到到某个元素
    def test_case_moveto_element(self):
        self.driver.get("http://www.baidu.com")
        element = self.driver.find_element(By.CSS_SELECTOR, '#s-usersetting-top')
        actions = ActionChains(self.driver).move_to_element(element)
        actions.perform()
        time.sleep(2)

    # 拖拽元素
    def test_case_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        source_ele = self.driver.find_element(By.XPATH, '//*[@id="dragger"]')
        target_ele = self.driver.find_element(By.XPATH, '//*[@class="item"][3]')  # //div[4]
        # 方法一：drag_and_drop 通过拖拽到目标元素
        # actions = ActionChains(self.driver).drag_and_drop(source_ele, target=target_ele)
        # actions.perform()
        # 方法二：click_and_hold 点击鼠标左键，不松开，release-在某个元素位置松开鼠标左键
        # ActionChains(self.driver).click_and_hold(source_ele).release(target_ele).perform()
        # 方法三：move_to_element 鼠标移到到某个元素
        ActionChains(self.driver).click_and_hold(source_ele).move_to_element(target_ele).release().perform()
        time.sleep(3)

    # 键盘操作
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        element = self.driver.find_element(By.XPATH, '//label[1]/input').click()
        actions = ActionChains(self.driver)
        actions.send_keys("yang yan").pause(2)
        actions.send_keys(Keys.BACKSPACE).pause(3)  # 删除键
        actions.perform()
        time.sleep(3)


# APP 端
class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # 滚动操作
    def test_touchaction_scroll(self):
        self.driver.get("http://www.baidu.com")
        element = self.driver.find_element(By.CSS_SELECTOR, '#kw')
        element.send_keys("selenium测试")
        search_element = self.driver.find_element_by_id('su')

        action = TouchActions(self.driver).tap(search_element)
        # action.perform()

        action.scroll_from_element(search_element, 0, 10000).perform()
        time.sleep(3)


# 表单操作
class TestForm():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("user_login").send_keys("yangyan")
        self.driver.find_element_by_id("user_password").send_keys("12343434")
        ele = self.driver.find_element_by_id("user_remember_me")
        self.driver.execute_script("arguments[0].click()", ele)  # 元素定位相互覆盖,所以我们将报错的定位点击事件按如下进行更改
        self.driver.find_element(By.XPATH, '//input[@name="commit"]').click()
        time.sleep(3)
