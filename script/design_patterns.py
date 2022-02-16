"""
设计模式
"""

import functools


class MySingleton(object):
    """
    使用 __new__ 关键字实现单例
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


def my_singleton(cls):
    """
    使用函数装饰器实现单例
    """
    _instance = {}

    @functools.wraps(cls)
    def my_singleton_inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return my_singleton_inner


@my_singleton
class TestMy(object):
    pass


class CHNHandler(object):
    def __init__(self):
        self.name = '大陆'


class USHandler(object):
    def __init__(self):
        self.name = '美国'


class Otherhandler(object):
    def __init__(self):
        self.name = '其他地区'


class WhereHandler(object):
    """
    工厂模式：定义一个用于创建对象的接口，根据不同的参数来决定实例化哪个子类
    """

    @classmethod
    def get_handler(cls, user_region):
        if user_region == 'CHN':
            return CHNHandler()
        elif user_region == 'US':
            return USHandler()
        else:
            return Otherhandler()


if __name__ == '__main__':
    # a = MySingleton()
    # b = MySingleton()
    # print(id(a) == id(b))

    # aa = TestMy()
    # bb = TestMy()
    # print(id(aa) == id(bb))

    my_handler = WhereHandler.get_handler('CHN')
    print(my_handler.name)
    my_handler = WhereHandler.get_handler('AUS')
    print(my_handler.name)
