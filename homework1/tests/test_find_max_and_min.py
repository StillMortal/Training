import os
from typing import Tuple

import pytest
from tasks.find_max_and_min import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (
            os.path.abspath(os.path.dirname(__file__)) + "/to_find_max_and_min",
            (109, -107),
        ),
    ],
)
def test_find_max_and_min(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
