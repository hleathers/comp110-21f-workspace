"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730407726"


def test_invert_random() -> None:
    """Test one."""
    word: dict[str, str] = {"a": "z", "b": "y"}
    assert invert(word) == {"z": "a", "y": "b"}


def test_invert_two() -> None:
    """Test two."""
    word: dict[str, str] = {}
    assert invert(word) == {}


def test_invert_three() -> None:
    """Test three."""
    word: dict[str, str] = {"c": "z", "d": "y"}
    assert invert(word) == {"z": "c", "y": "d"}


def test_favorite_color_one() -> None:
    """Test for favorite one."""
    color: dict[str, str] = {"Mark": "Pink", "Hannah": "Blue", "Annah": "Pink"}
    assert favorite_color(color) == {"Pink"}
    

def test_favorite_color_two() -> None:
    """Test for favorite two."""
    color: dict[str, str] = {"Markus": "Purple", "Henry": "Yellow", "Anna": "Yellow"}
    assert favorite_color(color) == {"Yellow"}

    
def test_favorite_color_three() -> None:
    """Test for favorite three."""
    color: dict[str, str] = {"Matt": "Orange", "Aubry": "Green", "Pat": "Orange"}
    assert favorite_color(color) == {"Orange"}


def test_count_one() -> None:
    """Test for favorite one."""
    another: list[str] = ["Blue", "Red", "Red"]
    assert count(another) == {"Blue": 1, "Red": 2}


def test_count_two() -> None:
    """Test for favorite two."""
    another: list[str] = ["Matt", "Vera", "Matt"]
    assert count(another) == {"Matt": 2, "Vera": 1}


def test_count_three() -> None:
    """Test for favorite three."""
    another: list[str] = ["Pink", "Pink", "Pink"]
    assert count(another) == {"Pink": 3}