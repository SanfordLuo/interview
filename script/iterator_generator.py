def test_iterator():
    my_list = [1, 2, 3]

    # 创建迭代器对象
    my_iter = iter(my_list)

    # # for循环遍历迭代器对象
    # for i in my_iter:
    #     print(i)

    # 使用next输出
    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))

    # 超出报错
    # print(next(my_iter))


class MyIterator(object):
    """
    创建一个返回数字的迭代器，初始值为1，逐步递增1
    """

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


def test_generator(num):
    """
    生成器实现斐波那契数列
    """
    a, b, count = 0, 1, 0
    while True:
        if count > num:
            return
        yield a
        a, b = b, a + b
        count += 1


if __name__ == '__main__':
    # test_iterator()

    # me = MyIterator()
    # my_iter = iter(me)
    # print(next(my_iter))

    my_generator = test_generator(10)
    print(next(my_generator))
    print(next(my_generator))
    print([_ for _ in my_generator])
