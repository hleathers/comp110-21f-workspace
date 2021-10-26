"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730407726"
from exercises.ex05.utils import only_evens


def test_only_evens() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_second_utils() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    assert only_evens(a_list) == [20, 30]
