"""
Armstrong number is a number that is the sum of its own digits
each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call

"""
from functools import lru_cache


def is_armstrong(number: int) -> bool:
    """Determines whether the number is an Armstrong number.

    Args:
        number: Number to check.

    Returns:
        True if successful, False otherwise.


    """
    digits = [int(i) for i in str(number)]

    @lru_cache(None)
    def a_num_in_a_power(digit):
        return pow(digit, len(digits))

    digits = [a_num_in_a_power(i) for i in digits]

    return number == sum(digits)
