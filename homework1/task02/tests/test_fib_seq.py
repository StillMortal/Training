from collections import Sequence

import pytest
from fib_sequence.fib_seq import check_fibonacci


@pytest.mark.parametrize(
    ["seq", "expected_result"],
    [
        ([], True),
        ((0,), True),
        ("01", True),
        ([0, 1, 1, 2, 3, 5], True),
        ((1,), False),
        ("23", False),
        ([1, 1, 2], False),
        ((1, 1, 2, 3, 4), False),
    ],
)
def test_fibonacci(seq: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(seq)

    assert actual_result == expected_result
