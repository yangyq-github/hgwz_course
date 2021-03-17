#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/16 17:14
# @File  : test_search.py
import unittest

__author__ = 'yangyanqin'


class Search:
    def search_fun(self):
        print("search")
        return True


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")
        cls.search = Search()

    def test_search1(self):
        print("test search1")
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test search2")
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test search3")
        assert True == self.search.search_fun()