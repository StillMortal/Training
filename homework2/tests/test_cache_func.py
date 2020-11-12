from typing import Any, Callable, Dict, List

import pytest

import homework2.tests.func_for_the_check as func
from homework2.tasks.cache_func import cache


@pytest.mark.parametrize(
    ["func_to_check", "args", "kwargs", "expected_result"],
    [
        (func.sum_of_parameters, [1, 3, 5], {}, 9),
        (func.sum_of_parameters, [-1, 1, 3], {}, 3),
        (func.args_len_plus_kwargs_len, [7], {"a": 5, "b": "c", "d": "e"}, 4),
    ],
)
def test_cache_func(
    func_to_check: Callable, args: List[int], kwargs: Dict, expected_result: Any
):
    actual_result = cache(func_to_check)(*args, **kwargs)

    assert actual_result == expected_result
