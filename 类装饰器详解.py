# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:      Decorator
   Description :   类装饰器详解
   Author :        Lx.Dong
   Date:           2019/04/11
-------------------------------------------------
   Update:
                   2019/04/11
-------------------------------------------------
"""


class LazyProperty(object):
    # 类装饰器所装饰的函数通过func进入装饰器中
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        # 装饰方法时调用__get__
        # print(instance)
        if instance is None:
            # 什么情况下instance是None的？
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            # print(self.func.__dict__)
            return value

    def __call__(self):
        # 装饰函数时调用__call__
        print('start')
        self.func()


class ConfigGetter(object):

    def __init__(self):
        pass

    @LazyProperty
    # 类方法调用
    def db_type(self):
        return "SSDB"


@LazyProperty
# 函数调用
def func():
    print('func')


config = ConfigGetter()

if __name__ == '__main__':
    print(config.db_type)
    func()