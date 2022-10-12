import time
from functools import wraps


def run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = int(time.time() * 1000)
        result = func(*args, **kwargs)
        end_time = int(time.time() * 1000)
        print(f"RUNTIME {end_time - start_time}")

        return result

    return wrapper


def run_time_params(params):
    def _wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = int(time.time() * 1000)
            result = func(*args, **kwargs)
            end_time = int(time.time() * 1000)
            print(f"RUNTIME {params} {end_time - start_time}")

            return result

        return wrapper

    return _wrapper


@run_time
def test_run_time():
    time.sleep(1)


@run_time_params(params="test")
def test_run_time_params():
    time.sleep(1)


if __name__ == '__main__':
    # test_run_time()
    test_run_time_params()
