"""
闭包 装饰器
"""


def bi_bao_out():
    name = 'sanford'

    def bi_bao_inner():
        return name

    return bi_bao_inner


if __name__ == '__main__':
    test = bi_bao_out()
    ret = test()
    print(ret)
