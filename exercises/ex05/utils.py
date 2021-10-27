"""List utility functions part 2."""

__author__ = "730407726"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Duplicate a list value."""
    even: list[int] = []
    for gh in xs:
        if gh % 2 == 0:
            even.append(gh)
    return even


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Duplicate a list value."""
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    i: int = start
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return []
    new: list[int] = []
    while i < end:   
        new.append(a_list[i])
        i += 1
    return new


def concat(y: list[int], p: list[int]) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    both: list[int] = y
    while i < len(p):
        both.append(p[i])
        i += 1
    return both