"""
闭包 装饰器
"""
import time
import functools


def bi_bao_outer():
    name = 'sanford'

    def bi_bao_inner():
        return name

    return bi_bao_inner


num_a = 3


def bi_bao_nonlocal():
    num_b = 4
    num_list = [6, 7, 8]

    def bi_bao_nonlocal_inner():
        # num_b 为不可变参数，进行自增时需要nonlocal声明,
        nonlocal num_b
        num_b += 1

        # num_list为可变参数，可直接append, 但是使用+=的话还是要声明的
        # nonlocal num_list
        num_list.append(9)
        # num_list += [3]

        return num_b, num_list

    return bi_bao_nonlocal_inner


def decorator_outer(func):
    def decorator_inner():
        begin_time = time.time()
        func()
        end_time = time.time()
        print('耗时:{0}'.format(end_time - begin_time))

    return decorator_inner


@decorator_outer
def test_decorator():
    time.sleep(3)
    print('执行完毕')


def decorator_factory(level):
    """
     参数化装饰器，装饰器工厂函数
     decorator_factory: 装饰器工厂函数
     decorator_outer_other：真正的装饰器
     decorator_inner_other：被装饰的函数
     增加@functools.wraps(func), 可以保持当前装饰器去装饰的函数的 __name__的值不变
    """

    def decorator_outer_other(func):

        @functools.wraps(func)
        def decorator_inner_other(sleep_time):
            if level == 'info':
                time.sleep(sleep_time)
                print('这是info级别的, 睡眠:{0}'.format(sleep_time))
            else:
                print('这是其他级别的')
            func(sleep_time)

        return decorator_inner_other

    return decorator_outer_other


@decorator_factory(level='info')
def test_decorator_other(sleep_time):
    print('执行完毕')


@decorator_factory(level='debug')
def test_decorator_other_1(sleep_time):
    print('执行完毕')


if __name__ == '__main__':
    # test = bi_bao_outer()
    # print(test)
    # print(test())

    # test_01 = bi_bao_nonlocal()
    # print(test_01())

    # test_decorator()

    # test_decorator_other(sleep_time=3)

    test_decorator_other_1(sleep_time=1)
