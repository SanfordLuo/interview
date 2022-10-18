"""
进程池
"""
import time
from multiprocessing import Pool


def func_test(num):
    ret = 0
    for i in range(num * 2):
        ret += 1
    # print(ret)


def run():
    begin = time.time()
    work_num = 4
    with Pool(work_num) as p:
        p.map(func_test, [i for i in range(10000)])
    end = time.time()

    print(end - begin)


def run_test():
    begin = time.time()
    for i in range(10000):
        func_test(i)
    end = time.time()

    print(end - begin)


if __name__ == '__main__':
    # 1.7813670635223389
    run()

    # 2.7031314373016357
    # run_test()
