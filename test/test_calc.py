#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/18 9:46
# @File  : test_calc.py
__author__ = 'yangyanqin'

# 测试计算器
import pytest, sys

sys.path.append("../")
from Chapter_Pytest_Actual_Combat.calc import Calculator


class TestCalc:
    @pytest.mark.add
    @pytest.mark.dependency(depends=["test_div"])
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize(("a", "b", "sum"), [
        (1, 2, 3),
        (0, 9, 9)
    ], ids=['int', '0'])  # ids 给用例起别名
    def test_add(self, a, b, sum):
        assert sum == Calculator().add(a, b)

    @pytest.mark.div
    @pytest.mark.dependency()
    @pytest.mark.first
    @pytest.mark.parametrize(("a", "b", "div"), [
        (1, 5, 0.5),
        (4, 2, 2)
    ])
    def test_div(self, a, b, div):
        assert div == Calculator().div(a, b)


class TestPytestAssume():
    def test_assume(self):
        print("登录操作")
        pytest.assume(1 == 2)
        print("搜索操作")
        pytest.assume(2 == 2)
        print("加购操作")
        pytest.assume(2 == 3)
