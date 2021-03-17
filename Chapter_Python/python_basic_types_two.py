#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/13 18:14
# @File  : python_basic_types.py
__author__ = 'yangyanqin'

import os, time
import urllib.request
import requests,pytest

# python 标准库
# os.removedirs("testdir")
print(os.listdir("./"))
print(os.getcwd())

print(os.path.exists("b"))
# if not (os.path.exists("b")):
#     os.mkdir("b")
#     if not (os.path.exists("b/test.txt")):
#         f=open("b/test.txt","w")
#         f.write("hele")
#         f.close()

# time 标准库
print(time.asctime())
print(time.time())
print(time.localtime())
now = time.time()
two_day_before = now - 60 * 60 * 24 * 2
tuple_time=time.localtime(two_day_before)
print(time.strftime('%Y{y}-%m{m}-%d{d} %H{h}:%M{i}:%S{s}',tuple_time).format(y='年',m='月',d='日',h='时',i='分',s='秒'))

#urllib.request
response= urllib.request.urlopen("https://www.baidu.com")
print(response.status)
# print(response.text)
# print(response.headers)

#常用的第三方库
r=requests.get("https://wwww.baidu.com")
print(r.headers)
