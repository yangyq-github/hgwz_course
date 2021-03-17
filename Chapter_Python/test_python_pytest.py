#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/16 17:48
# @File  : test_python_pytest.py
__author__ = 'yangyanqin'
import pytest


def func(x):
    return x + 1


# 使用pytest解释运行

#pytest-参数化
@pytest.mark.parametrize(('a','b'),[
    (1,2),
    (2,3),
    ("0","01")
])
def test_answer(a,b):
    assert func(a) == b



# fixture 作用:装饰器
@pytest.fixture()
def login():
    print("登录操作")
    username="jerry"
    return username

class TestDemo():
    def test_a(self,login):
        print(f"需要登录 +{login}")

    def test_b(self):
        print("不需要登录")

    def test_c(self,login):
        print(f"{login}")


# 使用python 解释器运行
if __name__ == '__main__':
    pytest.main(['test_python_pytest.py::TestDemo','-v'])
