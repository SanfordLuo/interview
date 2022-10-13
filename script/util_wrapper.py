"""
装饰器的示例
"""
import time
import logging
import asyncio
import json
from functools import wraps

logger = logging.getLogger("server")


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = int(time.time() * 1000)
        result = func(*args, **kwargs)
        end_time = int(time.time() * 1000)
        print(f"[RUNTIME] [{func.__name__}] [{end_time - start_time}ms]")

        return result

    return wrapper


def async_run_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = int(time.time() * 1000)
        result = await func(*args, **kwargs)
        end_time = int(time.time() * 1000)
        print(f"[RUNTIME] [{func.__name__}] [{end_time - start_time}ms]")

        return result

    return wrapper


def cache(key_format, expire=300):
    """
    缓存装饰器
    args,kwargs中需包含key_format中的键
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_name = func.__code__.co_varnames
            args_dict = dict(zip(args_name, args))
            args_dict.update(kwargs)
            key = key_format.format(**args_dict)

            # 读取缓存
            catch_result = ""
            if catch_result:
                result = json.loads(catch_result)["result"]
                print(f"读取缓存结果: {key}: {catch_result}: {expire}")
            else:
                result = func(*args, **kwargs)
                catch_result = json.dumps({"result": result})
                # 写入缓存
                print(f"写入缓存结果: {key}: {catch_result}: {expire}")
            return result

        return wrapper

    return decorator


@run_time
def test_run_time():
    time.sleep(3)


@async_run_time
async def test_async_run_time_00():
    await asyncio.sleep(2)
    return 0


@async_run_time
async def test_async_run_time_01():
    await asyncio.sleep(1)
    return 1


async def run_test_async():
    task_00 = test_async_run_time_00()
    task_01 = test_async_run_time_01()
    ret_00, ret_01 = await asyncio.gather(*[task_00, task_01])


@cache("test_catch:username:{username}")
def test_catch(username, ege):
    return username, ege


if __name__ == '__main__':
    # test_run_time()
    # asyncio.run(run_test_async())

    test_catch("luo", 28)
