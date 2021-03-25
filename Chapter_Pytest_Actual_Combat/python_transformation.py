#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/19 9:47
# @File  : python_transformation.py
__author__ = 'yangyanqin'

import json
#
# list_a=["小茉莉","小明","珠珠","丹丹"]
dict_a={"name":"哈哈1","性别":"女","ages":12}
#
# print("list_a 原始类型："+str(type(list_a)))
# list_a_json=json.dumps(list_a,ensure_ascii=False)
# print(list_a_json)
# print("list_a 转换后的类型："+str(type(list_a_json)))
#
#
# print("dict_a 原始类型："+str(type(dict_a)))
# dict_a_json=json.dumps(dict_a,ensure_ascii=False)
# print(dict_a_json)
# print("dict_a 转换后的类型："+str(type(dict_a_json)))
#
# string='''
#     {"name": "皇马", "性别": "女", "ages": 12}
# '''
# print(type(string))
#
# json_string = json.loads(string)
# print(type(json_string))

with open("json_01.json","w",encoding='UTF-8') as f:
    json.dump(dict_a,f,ensure_ascii=False)


with open("json.txt","r",encoding='UTF-8') as f:
    c=json.load(f)
    print(c)

