#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/29 18:41
# @File  : test_selenium_btc.py
# __author__ = 'yangyanqin'
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Chapter_selenium.base import Base
from time import sleep


class TestBtc(Base):

    def test_btc(self):
        self.driver.get("http://47.103.130.211/app/user/login")
        self.driver.find_element_by_link_text("验证码登录").click()
        # self.driver.find_element(By.XPATH, '//div[@class=" ant-tabs-tab"]').click()#邮箱验证
        # self.driver.find_element(By.CSS_SELECTOR, '#email').send_keys("ke_yao_02@163.com")
        self.driver.find_element(By.XPATH, '//div[@class="ant-tabs-tab-active ant-tabs-tab"]').click()  # 短信验证
        self.driver.find_element(By.CSS_SELECTOR, '#telephone').send_keys("18565444123")
        sleep(3)
        self.driver.execute_script('a= document.getElementById("verifyCode");a.removeAttribute("autocomplete")')
        self.driver.execute_script('a.value="123654"')
        sleep(10)
        self.driver.find_element_by_xpath('//button[@type="submit"]').submit()
        # self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        sleep(10)
