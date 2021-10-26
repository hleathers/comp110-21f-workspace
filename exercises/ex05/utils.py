"""List utility functions part 2."""

__author__ = "730407726"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Duplicate a list value."""
    gh: int = 0
    for gh in xs:
        if gh / 2 == 0:
            return xs
    return []


def sub(a_list: list[int], h: int) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    if len(a_list) == 0:
        return a_list
    while len(a_list) > i:
        if a_list[i] != 0:    
            return [h]
        i += 1
    return []


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