"""
concurrent.futures实现进程池线程池
"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def func_test(num):
    ret = 0
    for i in range(num * 2):
        ret += 1
    # print(ret)


def run_thread():
    begin = time.time()

    work_num = 4
    pool = ThreadPoolExecutor(work_num)
    for i in range(10000):
        pool.submit(func_test, i)

    end = time.time()

    print(end - begin)


def run_process():
    begin = time.time()

    work_num = 4
    pool = ProcessPoolExecutor(work_num)
    for i in range(10000):
        pool.submit(func_test, i)

    end = time.time()

    print(end - begin)


def run_test():
    begin = time.time()
    for i in range(10000):
        func_test(i)
    end = time.time()

    print(end - begin)


if __name__ == '__main__':
    # 0.07808756828308105
    run_thread()
    # 0.2031259536743164
    # run_process()
    # 2.827220916748047
    # run_test()
