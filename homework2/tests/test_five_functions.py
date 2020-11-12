import os
from typing import List

import pytest

import homework2.tasks.five_functions as func


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (
            os.path.abspath(os.path.dirname(__file__)) + "/data.txt",
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Werkstättenlandschaft",
                "Selbstverständlich",
                "Schicksalsfiguren",
                "Werkstättenlandschaft",
                "Vorausgeschickt",
                "Außerordentliche",
                "Friedensabstimmung",
            ],
        ),
        (
            os.path.abspath(os.path.dirname(__file__)) + "/data_to_check.txt",
            [
                "defg",
                "abc",
                "abcdɶ",
                "abcde",
                "abc",
                "abc",
                "ɵab",
                "def",
                "abcdefg",
                "abcdefgh",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(path_to_file: str, expected_result: List[str]):
    actual_result = func.get_longest_diverse_words(path_to_file)

    print(actual_result)
    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", "›"),
        (os.path.abspath(os.path.dirname(__file__)) + "/data_to_check.txt", "ɶ"),
    ],
)
def test_get_rarest_char(path_to_file: str, expected_result: str):
    actual_result = func.get_rarest_char(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", 5305),
        (os.path.abspath(os.path.dirname(__file__)) + "/data_to_check.txt", 13),
    ],
)
def test_count_punctuation_chars(path_to_file: str, expected_result: int):
    actual_result = func.count_punctuation_chars(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", 2972),
        (os.path.abspath(os.path.dirname(__file__)) + "/data_to_check.txt", 3),
    ],
)
def test_count_non_ascii_chars(path_to_file: str, expected_result: int):
    actual_result = func.count_non_ascii_chars(path_to_file)

    assert actual_result == expected_result


@pytest.mark.parametrize(
    ["path_to_file", "expected_result"],
    [
        (os.path.abspath(os.path.dirname(__file__)) + "/data.txt", "ä"),
        (os.path.abspath(os.path.dirname(__file__)) + "/data_to_check.txt", "ɵ"),
    ],
)
def test_get_most_common_non_ascii_char(path_to_file: str, expected_result: str):
    actual_result = func.get_most_common_non_ascii_char(path_to_file)

    assert actual_result == expected_result
