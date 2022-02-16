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


if __name__ == '__main__':
    a = MySingleton()
    b = MySingleton()
    print(id(a) == id(b))

    aa = TestMy()
    bb = TestMy()
    print(id(aa) == id(bb))
