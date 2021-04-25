#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/25 14:40
# @File  : test_main.py
# __author__ = 'yangyanqin'
import yaml


def test_main():
    with open("../driver_yaml/search.yaml", encoding='utf-8') as f:
        steps = yaml.safe_load(f)["search"]
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    print(step["by"], step["locator"])
                if "send" == action:
                    pass

        print(type(steps))


def test_replace():
    a = {"stock_name": "alibaba", "xxx": 1234}
    b = "*****${stock_name}****"
    for key, value in a.items():
        b = b.replace('${' + key + '}', repr(value))# repr 把对象转换成 str
    print(b)
