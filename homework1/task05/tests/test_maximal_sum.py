from typing import List

import pytest
from find_maximal_sum.find_maximal_sum import find_maximal_sum


@pytest.mark.parametrize(
    ["list_and_length", "expected_result"],
    [
        (([1, 2, 3, 99, -1, 102, 4, 5, 6], 3), 200),
        (([-1, -2, -3], 3), 0),
        (([-1, 97, -3], 3), 97),
    ],
)
def test_maximal_sum(list_and_length: (List[int], int), expected_result: int):
    actual_result = find_maximal_sum(*list_and_length)

    assert actual_result == expected_result
