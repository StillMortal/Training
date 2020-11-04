def check_power_of_2(a: int) -> bool:
    """Is a number a power of 2?"""
    return not (bool(a & (a - 1))) if a >= 0 else ValueError
