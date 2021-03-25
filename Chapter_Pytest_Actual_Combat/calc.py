#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/18 9:44
# @File  : calc.py
__author__ = 'yangyanqin'


# 实现计算器

class Calculator:

    def add(self, a, b):
        return a + b

    def div(self, a, b):
        return a / b

#yield 生成器，用next来获取下一个值
def fun():
    for i in range(10):
        print(f"i={i}")
        yield # return 同时相当于暂停并且记住上一次的执行位置
        print("end")

# a=fun()
# next(a)
# next(a)
# next(a)
