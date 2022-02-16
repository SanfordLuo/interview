import time


#  装饰器实现鉴权
def my_limit(region):
    def my_limit_(func):

        def _my_limit_(*args, **kwargs):
            if region == 'CHN':
                return func(*args, **kwargs)
            else:
                print('地区不符合')
                return

        return _my_limit_

    return my_limit_


@my_limit(region='CHN')
def test_my_limit(*args, **kwargs):
    print('欢迎您我的朋友')


# 装饰器打印日志
def my_log(func):
    def my_times_inner(*args, **kwargs):
        print('begin=====')
        func(*args, **kwargs)
        print('end=====')

    return my_times_inner


@my_log
def test_my_log():
    time.sleep(3)


class MyTest(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


def my_single_class(cls):
    _instance = {}

    def my_single_class_inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return my_single_class_inner


class CHNHandler(object):
    def __init__(self):
        self.name = 'CHN'


class OtherHandler(object):
    def __init__(self):
        self.name = 'OTHER'


class SomeHandler(object):

    @classmethod
    def get_handler(cls, region):
        if region == 'CHN':
            return CHNHandler()
        else:
            return OtherHandler()


@my_single_class
class TestMySingle(object):
    pass


if __name__ == '__main__':
    # test_my_limit()

    # test_my_log()

    # aa = MyTest()
    # bb = MyTest()
    # print(id(aa) == id(bb))

    # cc = TestMySingle()
    # dd = TestMySingle()
    # print(id(cc) == id(dd))

    my_handler = SomeHandler.get_handler('jjj')
    print(my_handler.name)
