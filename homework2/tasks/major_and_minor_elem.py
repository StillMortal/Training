"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List[int]) -> Tuple[int, int]:
    """Finds the most common and the least common elements.
    The most common element is the element that appears more than n // 2 times.
    The least common element is the element that appears fewer than other.

    Args:
        inp: Contains a list with elements.

    Returns:
        The most common and the least common elements.

    """
    num_and_its_quantity = {}

    for num in inp:
        if num in num_and_its_quantity:
            num_and_its_quantity[num] += 1
        else:
            num_and_its_quantity[num] = 1

    most_common_el = [0, 0]
    least_common_el = [0, float("inf")]

    for num in num_and_its_quantity:
        if num_and_its_quantity[num] > most_common_el[1]:
            most_common_el[0], most_common_el[1] = num, num_and_its_quantity[num]

        if num_and_its_quantity[num] < least_common_el[1]:
            least_common_el[0], least_common_el[1] = num, num_and_its_quantity[num]

    return most_common_el[0], least_common_el[0]
