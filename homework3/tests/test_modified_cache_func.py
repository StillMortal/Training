from typing import Any, Callable, List, Tuple

import pytest
from tasks.modified_cache_func import cache
from tests.func_for_the_check import func_for_the_test


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        ((func_for_the_test, 1), ([1, 3, 5], [-1, 1, 3]), 9),
        ((func_for_the_test, 1), ([-1, 1, 3], [1, 3, 5]), 3),
    ],
)
def test_cache_func(func_to_check: Callable, values: Tuple[List], expected_result: Any):
    cache_func = cache(*func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(*values[1])

    assert actual_result == actual_result2 == expected_result


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        ((func_for_the_test, 1), ([1, 3, 5], [-1, 1, 3], [0, 0, 0]), 9),
        ((func_for_the_test, 1), ([-1, 1, 3], [1, 3, 5], [0, 0, 0]), 3),
    ],
)
def test_cache_func_negative(
    func_to_check: Callable, values: Tuple[List], expected_result: Any
):
    cache_func = cache(*func_to_check)
    actual_result = cache_func(*values[0])
    actual_result2 = cache_func(*values[1])
    actual_result3 = cache_func(*values[2])

    assert not actual_result == actual_result2 == actual_result3 == expected_result
