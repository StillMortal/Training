from typing import Any, Callable, List

import pytest
from tasks.cache_func import cache
from tests.func_for_the_check import func_for_the_test


@pytest.mark.parametrize(
    ["func_to_check", "values", "expected_result"],
    [
        (func_for_the_test, [1, 3, 5], 9),
        (func_for_the_test, [-1, 1, 3], 3),
    ],
)
def test_cache_func(func_to_check: Callable, values: List[int], expected_result: Any):
    actual_result = cache(func_to_check)(*values)

    assert actual_result == expected_result
