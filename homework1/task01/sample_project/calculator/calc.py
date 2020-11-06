def check_power_of_2(a: int) -> bool:
    """Whether the number is a power of 2.

    Args:
        a: Number.

    Returns:
        True if successful, False otherwise.

    """
    return not (bool(a & (a - 1))) if a != 0 else False
