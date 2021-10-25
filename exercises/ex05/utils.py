"""List utility functions part 2."""

__author__ = "730407726"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    if xs[i] / 2:
        return xs
    while i < len(xs):
        if xs[i] != 0:    
            return []
        i += 1
    return xs


def sub(a_list: list[int], h: int) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    if len(a_list) == 0:
        return a_list
    max: int = a_list[0]
    while len(a_list) > max:
        if a_list[i] != 0:    
            return [h]
        i += 1
    return [max]


def concat(y: list[int], p: list[int]) -> list[int]:
    """Duplicate a list value."""
    i: int = 0
    if len(y) == 0:
        return y
    while i < len(p):
        if y[i] != 0:    
            return p
        i += 1
    return p