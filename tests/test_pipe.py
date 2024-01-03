"""Provides with tests for the composite feature.
"""
import pytest
import re
from functools import partial

from compoz import pipe


@pytest.mark.parametrize(
    "text, limit, to_filter, expected",
    [
        ("bananas are yellow", 10, "a", "bnns re ye"),
        ("you shall not pass", 10, "o", "yu shall n"),
    ],
    indirect=False,
)
def test_pipe_should_return_a_filtered_then_delimited_string(
        text: str,
        limit: int,
        to_filter: str,
        expected: str,
):
    def delimit_string(string: str, lmt: int) -> str:
        return string[0:lmt]

    def filter_string(string: str, to_fltr: str) -> str:
        return re.sub(to_fltr, '', string)

    composite_func = pipe([
        partial(filter_string, to_fltr=to_filter),
        partial(delimit_string, lmt=limit),
    ])
    assert composite_func(text) == expected
