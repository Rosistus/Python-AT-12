from typing import Callable, Any


def memoize(func: Callable) -> Any:
    data = {}

    def wrapped_func(number):
        if number not in data.keys():
            data[number] = func(number)
        return data[number]
    
    return wrapped_func


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(40))