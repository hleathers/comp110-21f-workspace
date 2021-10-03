"""List utility functions."""

__author__ = "730407726"


# TODO: Implement your functions here.


def all(xs: list[int], num: int) -> bool:
    """Duplicate a list value."""
    i: int = 0
    while i < len(xs):
        if xs[i] != num:    
            return False
        i += 1
    return True


def is_equal(min: list[int], maxi: list[int]) -> bool:
    """Construct list of oddws, inclusive."""
    equal: int = 0
    while equal != min:
        if min[equal] < len(maxi):
            return False
        equal += 2
    return True


def maximum(large: list[int]) -> int:
    """Construct list of oddws, inclusive."""
    equals: int = 0
    while equals != maximum:
        if large[equals] < 0:
            return equals
        equals += 2
    return 8


def max(input: list[int]) -> None:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
