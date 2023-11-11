import time
from typing import Callable, Any


def timer(func: Callable) -> Any:

    def wrapped_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = round(end_time - start_time, 5)
        print("Функция работала", run_time, "секунд")

        return result
    return wrapped_func


def memoize(func: Callable) -> Any:
    data = {}

    def wrapped_func(number):
        if number not in data.keys():
            data[number] = func(number)
        return data[number]

    return wrapped_func


def validate_args(func: Callable) -> Callable:

    def wrapped_func(*args) -> Any:
        if len(args) < 1:
            print('Not enough arguments')
            return

        if len(args) > 1:
            print('Too many arguments')
            return

        inp = args[0]
        if not isinstance(inp, int):
            print('Wrong types')
            return

        if inp < 0:
            print('Negative argument')
            return
        else:
            return func(inp)

    return wrapped_func




@validate_args
def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibon = fibonacci
new_fibon = timer(fibon)
my_fibon = new_fibon(31)
print(timer(fibon))
new_mem = timer(memoize(fibon))
my_mem = new_mem(31)
print(my_mem)


