#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/24 17:32
# @File  : test_cal_new.py
__author__ = 'yangyanqin'

# 测试计算器--数据驱动方式
import pytest, sys, yaml

sys.path.append("../")
from Chapter_Pytest_Actual_Combat.calc import Calculator

with open("datas/cal_data.yml", encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    addkeys = datas['add'].keys()
    addvalues = datas['add'].values()

    divkeys = datas['div'].keys()
    divvalues = datas['div'].values()


class TestCalNew():
    @pytest.mark.parametrize(('a', 'b', 'result')
        , addvalues, ids=addkeys)
    def test_add(self, a, b, result):
        assert result == Calculator().add(a, b)

    @pytest.mark.parametrize(('a', 'b', 'result')
        , divvalues, ids=divkeys)
    def test_div(self, a, b, result):
        assert result == Calculator().div(a, b)

@pytest.mark.Env
class TestEnv():
    def test_case(self, cmdoption):
        print("测试环境的验证")
        env, datas = cmdoption
        print(f"环境：{env},数据：{datas}")
        ip = datas['env']['ip']
        port = datas['env']['port']
        print("http://"+str(ip)+":"+str(port))


mydatas=[[1,2,3],[0.9,0.1,1]]
myids=['整数','浮点数']
# param1 需要和conftest 中处理的param1 保持一致
class TestCalNewOne():
    def test_add(self, param1):
        print(f"param={param1}")
        print("动态生成测试用例")
        # assert result == Calculator().add(a, b)