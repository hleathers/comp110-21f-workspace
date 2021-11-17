"""Practice with dictionaries."""

__author__ = "730407729"

# Define your functions below


def invert(word: dict[str, str]) -> dict[str, str]:
    """Invert function."""
    result: dict[str, str] = {}
    for x in word:
        result[word[x]] = x
    if len(word) != len(result):
        raise KeyError("Error")
    return result


def favorite_color(color: dict[str, str]) -> str:
    """Favorite color."""
    favorite: str = ""
    new: dict[str, int] = {}
    for person in color:
        if color[person] in new:
            new[color[person]] += 1
        else:
            new[color[person]] = 1
    max: int = 0
    for most in new:
        if new[most] > max:
            max = new[most]
            favorite = most
    return favorite


def count(another: list[str]) -> dict[str, int]:
    """Count function."""
    store: dict[str, int] = {}
    for value in another:
        if value in store:
            store[value] += 1
        else:
            store[value] = 1
    return store