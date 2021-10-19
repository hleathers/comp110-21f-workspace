"""List utility functions."""

__author__ = "730407726"


# TODO: Implement your functions here.

def main() -> None:
    all([1], 2)
    is_equal([1], [0])
    max([1, 2, 3, 4, 5])


def all(xs: list[int], num: int) -> bool:
    """Duplicate a list value."""
    i: int = 0
    if len(xs) == 0:
        return False
    while i < len(xs):
        if xs[i] != num:    
            return False
        i += 1
    return True


def is_equal(min: list[int], maxi: list[int]) -> bool:
    """Construct equal."""
    equal: int = 0
    if min == maxi:
        return True
    while min != maxi:
        if min[equal] < len(maxi):
            return False
        equal += 1
        while len(min) == 0:
            return False
    return False


def max(large: list[int]) -> int:
    """Construct max."""
    max: int = 0
    i: int = 0
    if len(large) == 0:
        raise ValueError("max() arg is an empty List")
    while len(large) > i:
        if max < large[i]:
            max = large[i]
        i += 1
    return max


if __name__ == "__main__":
    main()