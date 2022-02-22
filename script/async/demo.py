import time
import asyncio


def test_0(sleep_time):
    time.sleep(sleep_time)
    print(time.time())


def run_0():
    begin = time.time()
    print('0: begin=====')

    for i in range(3):
        test_0(i)

    print('0: end=====')
    end = time.time()
    print('0: times: {}'.format(end - begin))


async def test_1(sleep_time):
    await asyncio.sleep(sleep_time)
    print(time.time())


def run_1():
    begin = time.time()
    print('1: begin=====')

    # 创建事件循环
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # 获取事件循环
    # loop = asyncio.get_event_loop()

    # 事件队列
    tasks = []

    for i in range(3):
        # 将异步函数调用加入事件队列
        tasks.append(loop.create_task(test_1(i)))

    # 执行事件队列，直到最晚的一个事件被处理完毕结束
    loop.run_until_complete(asyncio.wait(tasks))

    # 手动关闭loop实例
    loop.close()

    print('1: end=====')
    end = time.time()
    print('1: times: {}'.format(end - begin))


if __name__ == '__main__':
    run_0()
    run_1()
