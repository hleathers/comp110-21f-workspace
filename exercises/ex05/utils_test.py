"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730407726"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_two() -> None:
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_three() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub_three() -> None:
    a_list: list[int] = [16, 17, 18, 19]
    start: int = 1
    end: int = 2
    assert sub(a_list, start, end) == [17]


def test_sub_two() -> None:
    a_list: list[int] = [15]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == []


def test_concat() -> None:
    p: list[int] = [2, 3, 5]
    y: list[int] = [12, 6, 45]
    assert concat(p, y) == [2, 3, 5], [12, 6, 45]
