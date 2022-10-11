import asyncio


async def func_00():
    print("===== func_00 start=====")
    await asyncio.sleep(3)
    print("===== func_00 end=====")
    return 0


async def func_01():
    print("===== func_01 start=====")
    await asyncio.sleep(1)
    print("===== func_01 end=====")
    raise "error"
    # return 1


async def run():
    task_00 = func_00()
    task_01 = func_01()
    ret_00, ret_01 = await asyncio.gather(*[task_00, task_01], return_exceptions=True)
    print(ret_00, ret_01)


if __name__ == '__main__':
    ret = run()
    asyncio.run(ret)
