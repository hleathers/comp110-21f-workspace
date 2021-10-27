"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730407726"
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Test even."""
    xs: list[int] = [1, 2, 3]
    assert only_evens(xs) == [2]


def test_only_evens_two() -> None:
    """Test even."""
    xs: list[int] = [4, 4, 4]
    assert only_evens(xs) == [4, 4, 4]


def test_only_evens_three() -> None:
    """Test even."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_sub() -> None:
    """Test even."""
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [20, 30]


def test_sub_three() -> None:
    """Test even."""
    a_list: list[int] = [16, 17, 18, 19]
    start: int = 1
    end: int = 2
    assert sub(a_list, start, end) == [17]


def test_sub_two() -> None:
    """Test even."""
    a_list: list[int] = [15]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == []


def test_concat() -> None:
    """Test even."""
    p: list[int] = [2, 3, 5]
    y: list[int] = [12, 6, 45]
    assert concat(p, y) == [2, 3, 5, 12, 6, 45]


def test_concat_two() -> None:
    """Test even."""
    p: list[int] = [8, 9]
    y: list[int] = [11, 13]
    assert concat(p, y) == [8, 9, 11, 13]


def test_concat_three() -> None:
    """Test even."""
    p: list[int] = [44, 55]
    y: list[int] = [66, 77]
    assert concat(p, y) == [44, 55, 66, 77]
