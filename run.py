#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/16 17:19
# @File  : run.py.py
import unittest

__author__ = 'yangyanqin'

test_dir='./test'
discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
unittest.TextTestRunner().run(discover)
