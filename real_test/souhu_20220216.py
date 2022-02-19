"""
搜狐 20220216
1. 装饰器实现用户的权限
2. 生成器实现斐波那契数列
"""


def limit_region(region=None):
    def func_outer(func):
        def func_inner(*args, **kwargs):
            if region != 'CHN':
                print('地区不符合')
                return
            else:
                return func(*args, **kwargs)

        return func_inner

    return func_outer


@limit_region(region='CHN')
def test_limit_region(*args, **kwargs):
    print('地区符合 有权限')


def gen_fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield a
        a, b = b, a + b
        n += 1
    return


if __name__ == '__main__':
    # test_limit_region()

    ret = gen_fib(10)
    print(list(ret))
