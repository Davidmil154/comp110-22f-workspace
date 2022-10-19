"""EX07 - Dict Functions Test."""


__author__ = "730622383"

from exercises.ex07.dictionary import invert, count, favorite_color
import pytest

def test_invert_normal() -> None:
    """Checks that normal behavior with a dict is fine."""
    test_dict: dict[str,str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert(invert(test_dict)) == {'z': 'a', 'y': 'b', 'x': 'c'}

def test_invert_one_value() -> None:
    """Checks that invert works with a list with only one key value pair."""
    test_dict: dict[str, str] = {'apple': 'cat'}
    assert(invert(test_dict)) == {'cat': 'apple'}

def test_invert_key_error() -> None:
    """Checks that invert returns a key error if two of the same keys are attempted to be created."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
        invert(test_dict)

def test_favorite_color_normal() -> None:
    """Testing favorite color with a normal list."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert(favorite_color(test_dict)) == "blue"

def test_favorite_color_tie() -> None:
    """Testing favorite color with two tied colors."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "David": "yellow"}
    assert(favorite_color(test_dict)) == "yellow"

def test_favorite_color_all_one() -> None:
    """Tests that favorite color works with only one color."""
    test_dict: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    assert(favorite_color(test_dict)) == "blue"

def test_count_normal() -> None:
    """Tests that count works with 2 colors."""
    test_list: list[str] = ["blue", "blue", "yellow"]
    assert(count(test_list)) == {"blue": 2, "yellow": 1}

def test_count_several_colors() -> None:
    """Tests that count works with a bunch of colors."""
    test_list: list[str] = ["blue","orange","blue","pink","pink","green"]
    assert(count(test_list)) == {"blue": 2, "orange": 1, "pink": 2, "green": 1}

def test_count_empty_list() -> None:
    """Tests that count works with an empty list."""
    test_list: list[str] = []
    assert(count(test_list)) == {}