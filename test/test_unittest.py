#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/16 17:15
# @File  : test_unittest.py
__author__ = 'yangyanqin'

import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear down class")

    def test_upper(self):
        print("test upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.islower())

    def test_split(self):
        print("test spit")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)