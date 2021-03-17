#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/17 10:40
# @File  : test_python_allure.py
__author__ = 'yangyanqin'
# Allure 测试框架

import pytest
import allure

TEST_CASE_LINK = "https://www.baidu.com"


@allure.title("链接测试")
@allure.story("link")
@allure.testcase(TEST_CASE_LINK, "Test case title")
def test_link():
    pass


@allure.feature("搜索模块")
class TestSearch():
    @allure.title("第一个测试用例")
    def test_search_01(self):
        print("case_01")

    @allure.title("第二个测试用例")
    def test_search_02(self):
        print("case_02")


@allure.feature('登录模块')
class TestLogin():
    @allure.title("登录成功")
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录： 测试用例，登录成功")
        pass

    @allure.title("登录失败")
    @allure.story("登录失败")
    def test_login_fail(self):
        print("这是登录： 测试用例，登录失败")
        pass

    @allure.title("登录失败--缺失用户名")
    @allure.story("用户名缺失")
    def test_login_no_username(self):
        print("这是登录： 测试用例，用户名缺失")
        pass

    @allure.title("登录失败--缺失密码")
    @allure.story("密码缺失")
    def test_login_no_passwd(self):
        with allure.step("点击用户"):
            print("输入用户名")
        with  allure.step("点击密码"):
            print("请输入密码")
        print("点击登录")
        with allure.step("点击登录后登录失败"):
            assert '1' == 1
            print("登录失败")

        pass


# 设置测试用例级别
@allure.severity(allure.severity_level.NORMAL)
def test_with_normal_severity_no_class():
    pass


@allure.severity(allure.severity_level.NORMAL)
@allure.feature("level")
class TestLevel():
    def test_default(self):
        pass

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_with_trivial_severity(self):
        pass

    @allure.severity(allure.severity_level.MINOR)
    def test_with_minor_severity(self):
        pass

    @allure.severity(allure.severity_level.NORMAL)
    def test_with_normal_severity(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_with_critical_severity(self):
        pass

    @allure.severity(allure.severity_level.BLOCKER)
    def test_with_blocker_severity(self):
        pass


# allure 报告中嵌入文本、图片、视频等资源
@allure.feature("资源")
class TestAttach():

    @allure.title("文本")
    def test_attach_text(self):
        allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

    @allure.title("html")
    def test_attach_html(self):
        allure.attach(r"<body>这是一段htmlbody块</body>", name="html测试块", attachment_type=allure.attachment_type.HTML)

    @allure.title("图片")
    def test_attach_photo(self):
        with open(r"C:\Users\JS-Test-001\Pictures\Camera Roll\kyc.jpg","rb") as f:
            allure.attach(f.read(), name="这是一个图片",
                          attachment_type=allure.attachment_type.JPG)

    @allure.title("视频")
    def test_attach_video(self):
        with open(r"G:\个人\霍格沃兹测开课程\课程视频\第二章 Linux与Bash课程\第五节 Linux进阶命令.mp4", "rb") as f:
            allure.attach(f.read(), name="这是一个视频文件",
                          attachment_type=allure.attachment_type.MP4)


if __name__ == '__main__':
    pytest.main()

