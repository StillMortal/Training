"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.

def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable


def cache(func: Callable) -> Callable:
    """Caches the function.

    Args:
        func: A function that needs to be cached.

    Returns:
        Callable.

    """
    used_parameters = {}

    def cache_func(*args, **kwargs):
        parameters = args + tuple(i for j in kwargs.items() for i in j)
        if parameters not in used_parameters:
            used_parameters[parameters] = func(*args, **kwargs)

        return used_parameters[parameters]

    return cache_func


def func(*args, **kwargs):
    print(args)
    print(kwargs)
    return 1


cache(func)(7, a=5, b="c")
