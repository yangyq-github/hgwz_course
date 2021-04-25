#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/25 14:40
# @File  : test_main.py
# __author__ = 'yangyanqin'
import yaml


def test_main():

    with open("../driver_yaml/main.yaml", encoding='utf-8') as f:
        steps = yaml.safe_load(f)

        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if "click" == action:
                    print("find action")
                if "send" == action:
                    pass

        print(steps)
