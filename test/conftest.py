#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/23 18:47
# @File  : conftest.py
from _pytest.python import Metafunc

__author__ = 'yangyanqin'

from typing import List
import pytest, yaml


@pytest.fixture(params=['yang', 'linda'])
def login(request):
    print(request.param)
    print("登录方法")
    yield ['username', 'passworld']  # 激活后续操作，作用同 teardown
    print("退出登录")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")  # nodeid 整个用例的名称
        # 为测试用例添加标签
        if 'add' in item.nodeid:
            item.add_marker(pytest.mark.add)


# parser：用户命令行参数与ini文件值的解析器
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group将下面所有的option 都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


# 处理命令行传来的参数，设置成 fixture，将test环境和dev环境或者其他环境下的数据
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='env')
    if myenv == 'env':
        dataspath = './datas/dev/data.yml'
    if myenv == 'test':
        dataspath = './datas/test/data.yml'

    with open(dataspath, encoding='UTF-8') as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过方法动态的生成测试用例
#addvalues/addkeys需要跟定义参数的列表名称保持一致
def pytest_generate_tests(metafunc: Metafunc):
    if 'param1' in metafunc.fixturenames:
        metafunc.parametrize('param1',
                             metafunc.module.addvalues,
                             ids=metafunc.module.addkeys,
                             scope='function')
