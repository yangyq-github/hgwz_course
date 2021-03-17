#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/17 10:02
# @File  : test_data.py
__author__ = 'yangyanqin'
"""pytest 参数化用例"""
import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(["a", "b"], [
        (10, 20),
        (3, 9),
        (0, 0)
    ])
    def test_data(self, a, b):
        print(a + b)


class TestData2:
    @pytest.mark.parametrize(["a", "b", "c"], yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b, c):
        print(a + b + c)


class TestDemo_yaml:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):

        if "test" in env:
            print(env["test"])
            print("这是测试环境")

        elif "dev" in env:
            print("这是开发环境")

        print(yaml.safe_load(open("./env.yml")))