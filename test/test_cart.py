#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/23 19:23
# @File  : test_cart.py
import pytest

__author__ = 'yangyanqin'


def test_cart1(login):
    print("购物车用例-1")


def test_cart2(login):
    print("购物车用例-2")


# 参数化结合 fixture 使用
# 情况一：传入值和数据
# 情况二：传入一个fixture方法，将数据传入到fixture方法中，fixture方法使用request参数来接收这组数据，在方法体里面使用request.param 来使用这个数据

@pytest.mark.parametrize('login', [
    (1, 2),
    (9, 10)
], indirect=True)
def test_cart3(login):
    print("购物车用例-3")


# 笛卡儿积倍的参数化
@pytest.mark.parametrize('a', [4, 6, 7])
@pytest.mark.parametrize('b', [8, 9, 10])
def test_data(a, b):
    print(a, b)
