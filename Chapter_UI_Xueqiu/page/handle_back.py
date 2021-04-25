#!/usr/bin/python3
# coding : utf-8
# @Time  : 2021/4/25 11:14
# @File  : handle_back.py
# __author__ = 'yangyanqin'
import logging,allure

from selenium.webdriver.common.by import By


def handle_black(func):
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")
        ]
        _max_err_num = 3
        _error_num = 0
        # 局部导入，可以避免同一个方法多个模块中多次导入，陷入死循环中
        from Chapter_UI_Xueqiu.page.base_page import BasePage
        instance: BasePage = args[0]

        try:
            # 打印函数名称和查找的信息
            logging.info("run" + func.__name__ + "\n args: \n" + repr(args[1:]) + "\n" + repr(kwargs))
            # 如果元素找到，就清空 error 计算
            element = func(*args, **kwargs)
            _error_num = 0
            return element
        except Exception as e:
            # 出现异常保存截图
            instance.screenshot("tmp.png")
            with open("tmp.png","rb") as f:
                content=f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            logging.error("element not found,handle black list")

            instance.set_implicitly_wait(1)
            # 装饰器特性：传入的第0个参数为self，所以可以使用以下方法获取self参数
            # instance = args[0]
            # 如果没有找到，则进行黑名单处理
            if instance._error_num > instance._max_err_num:
                # 如果error次数大于指定值，清空 error 次数并抛出异常
                instance._error_num = 0
                raise e
            instance._error_num += 1
            for ele in instance._black_list:
                # 对黑名单进行点击
                eles = instance.finds(ele)
                if eles.__len__() > 0:
                    eles[0].click()
                    return wrapper(*args, **kwargs)
            raise ValueError("元素不在黑名单中")

    return wrapper
