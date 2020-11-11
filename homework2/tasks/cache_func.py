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

    def cache_func(*args):
        args = tuple(i for i in args)
        if args not in used_parameters:
            used_parameters[args] = func(*args)

        return used_parameters[args]

    return cache_func
