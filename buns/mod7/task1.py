import random
from typing import Callable, Any


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


# @validate_args
# def somefunc(number):
#     result = number + random.randint(-number, 100)
#     return 'Ваш психологический возраст: {} лет!'.format(result)
#
#
# ans = somefunc(24)
# print(ans)
