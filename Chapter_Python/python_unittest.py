#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/16 15:42
# @File  : python_unittest.py
__author__ = 'yangyanqin'
import unittest
from uitl.HTMLTestRunner_PY3 import HTMLTestRunner


def demo_method(a, b, x):
    if (a > 1 and b == 0):
        x = x / a
    if (a == 2 or x > 1):
        x = x + 1
    return x


# print(demo_method(3,0,4))

# class TestStringMethods(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print("setUp")
#
#     def tearDown(self) -> None:
#         print("tearDown")
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         print("set up class")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("tear down class")
#
#     def test_upper(self):
#         print("test upper")
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         print("test isupper")
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.islower())
#
#     def test_split(self):
#         print("test spit")
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         with self.assertRaises(TypeError):
#             s.split(2)


# if __name__ == '__main__':
# #     unittest.main()
# #
# #     suit = unittest.TestSuite()
# #     suit.addTest(TestStringMethods("test_upper"))
# #     unittest.TextTestRunner().run(suit)
#
#     suit_class=unittest.TestLoader().loadTestsFromTestCase(TestSearch)
#     suit_class_02=unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
#     suit = unittest.TestSuite([suit_class,suit_class_02])
#     unittest.TextTestRunner().run(suit)

report_title = "用例执行报告 我的标题"
desc = "用于展示修改样式后的 HTMLTestRunner"
report_file = "./result.html"

test_dir = '../test'

discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
with open(report_file, 'wb') as f:
    runner = HTMLTestRunner(
        stream=f,
        title=report_title,
        description=desc
    )
    runner.run(discover)
# unittest.TextTestRunner().run(discover)
