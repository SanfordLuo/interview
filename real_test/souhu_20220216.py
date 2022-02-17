"""
搜狐 20220216
装饰器实现用户的权限
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
def func_test(*args, **kwargs):
    print('地区符合 有权限')


if __name__ == '__main__':
    func_test()
