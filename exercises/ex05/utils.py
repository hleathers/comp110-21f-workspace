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
    i: int = start
    if start < 0:
        
    if len(a_list) == 0:
        return a_list
    new: list[int] = []
    while i < end:   
        new.append(a_list[i])
    return new


def concat(y: list[int], p: list[int]) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    if len(y) == 0:
        return y
    while i < len(p):
        if y[i] != 0:    
            return p
        i += 1
    return []