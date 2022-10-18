import time
from gevent import pool


def func_test(num):
    ret = 0
    for i in range(num * 2):
        ret += 1
    # print(ret)


def run_gevent():
    begin = time.time()
    p = pool.Pool(4)

    p.map(func_test, [_ for _ in range(10000)])

    end = time.time()

    print(end - begin)


if __name__ == '__main__':
    run_gevent()
