#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/3/13 18:14
# @File  : python_basic_types.py
__author__ = 'yangyanqin'

import random, json

a = 1
# print(id(a))  # id可以打印变量的存储地址
#
# compile_a = 0.2j
# b = "123" "3232"
# print(b[0:5:2])
# c = [1, 2, 3]
# print(c[0])

# 1. 求1~100的求和
# 2. 加入分支结构实现1~100之间的偶数求和
# 3. 使用python实现1~100之间的偶数求和
# sum = 0
# for i in range(0, 101, 2):
#     # if i % 2 == 0:
#     sum += i
# print(sum)
#
# i = 1
# while i < 101:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print(sum)

"""猜数字游戏
计算机给出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分辨
给出提示大一点/小一点/猜对了
"""

# num = random.randint(1, 100)
# while True:
#     print("请输入一个数字：")
#     person = int(input())
#     if person > num:
#         print("小一点")
#     elif person < num:
#         print("大一点")
#     elif person == num:
#         print("猜对了")
#         break


func = lambda x: x * 2
print(func(4))

# 列表
list_01 = [3, 1, 5, 6]
list_02 = [9, 0, 7]
list_01.extend(list_02)
print(list_01)

# 列表推导式
list_03 = [i ** 2 for i in range(1, 100) if i % 2 == 0]
print(list_03)
# 列表推导式-嵌套
list_04 = [str(i) + "*" + str(j) + "=" + str(i * j) for i in range(1, 10) for j in range(1, 10)]
print(list_04)

# 结合
a = {1, 2, 3}
b = {1, 3, 8}
print(a.intersection(b))
print(a.difference(b))

# python 输入输出
name = "小黄"
age = 45
dict = {"name": "小李", "age": 66}
print("my name is %s" % name)
print("my name is %s,my age is %d" % (name, age))
print("my name is {0},my age is {1},{0}{1}".format(name, age))
print("my name is {name},age is {age}".format(**dict))
print(f"my name is {dict['name'].upper()}")
print(f"result is {(lambda x: x + 1)(9)}")
# 文件读取
# file=open("data.txt")
# print(file.readlines())
# print(file.readable())
# file.close()


# with open("data.txt","a") as f:
# #     f.write("\n你好")

data = {
    "name": ["jerry", "nickname"],
    "age": "24",
    "gender": "female"
}
data1 = json.dumps(data)  # str
data2 = json.loads(data1)  # json


# with open("data.txt","a") as f:
#     json.dump(data,f)

# 错误与异常

class MyException(Exception):
    def __init__(self,msg):
        print(f"这是一个异常：{msg}")

def set_age(num):
    if num < 0 or num > 200:
        # raise ValueError(f"年龄不能小于{0}")
        raise MyException(f"值错误:{num}")
    else:
        print(f"设置的年龄为{num}")

# set_age(-1)

# 面向对象编程
class Person():
    name="default"
    age=0
    gender="male"
    weight=0
    def __init__(self):
    #  构造方法
        pass

    def set_param(self,name):
        self.name=name

    @classmethod
    def eat(self):
        print("eating")

    def play(self):
        print("playing")

    def jump(self):
        print("jump")

zs=Person()
zs.set_param('张三')
print(zs.name)
Person.eat()