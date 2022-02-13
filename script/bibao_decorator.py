"""
闭包 装饰器
"""


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


if __name__ == '__main__':
    # test = bi_bao_outer()
    # print(test)
    # print(test())

    test_01 = bi_bao_nonlocal()
    print(test_01())
