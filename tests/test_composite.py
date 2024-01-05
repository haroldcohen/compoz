"""Provides with tests for the composite feature.
"""
import pytest
import re
from functools import partial

from compoz import composite


@pytest.mark.parametrize(
    "number",
    [
        2,
        3,
    ],
    indirect=False,
)
def test_composite_should_return_a_number_plus_3(number: int):
    def add_1(num: int) -> int:
        return num + 1

    def add_2(num: int) -> int:
        return num + 2

    expected_result = number + 3

    composite_add = composite(add_1, add_2)
    assert composite_add(number) == expected_result


@pytest.mark.parametrize(
    "text, limit, to_filter, expected",
    [
        ("bananas are delicious", 10, "a", "bnns re de"),
        ("fruits are awesome", 4, "i", "frut"),
    ],
    indirect=False,
)
def test_composite_should_return_a_filtered_then_delimited_string(
        text: str,
        limit: int,
        to_filter: str,
        expected: str,
):
    def delimit_string(string: str, lmt: int) -> str:
        return string[0:lmt]

    def filter_string(string: str, to_fltr: str) -> str:
        return re.sub(to_fltr, '', string)

    composite_func = composite(
        partial(delimit_string, lmt=limit),
        partial(filter_string, to_fltr=to_filter),
    )
    assert composite_func(text) == expected
