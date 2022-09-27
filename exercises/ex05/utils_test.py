"""EX05 - List Utility Functions Test."""


__author__ = "730622383"

from exercises.ex05.utils import only_evens, concat, sub

def test_only_evens_empty_list() -> None:
    """Checks that an empty list given returns an empty list. edge case."""
    test_list: list[int] = []
    assert only_evens(test_list) == []

def test_only_evens_mostly_odd() -> None:
    """Checks that a list of mostly odds still returns its evens."""
    test_list: list[int] = [1,2,3,5,7,9,10,13]
    assert only_evens(test_list) == [2,10]

def test_only_evens_all_even() -> None:
    """Tests that a list of mostly evens still returns all its evens."""
    test_list: list[int] = [2,4,6,8,9,11,12,14]
    assert only_evens(test_list) == [2,4,6,8,12,14]


def test_concat_list2_longer() -> None:
    """Tests that concat returns correctly when list2 is longer than list1."""
    test_list1: list[int] = [1,2,3]
    test_list2: list[int] = [2,3,4,5,6,7,8,9]
    assert concat(test_list1,test_list2) == [1,2,3,2,3,4,5,6,7,8,9]

def test_concat_list1_longer() -> None:
    """Tests that concat returns correctly when list1 is longer than list2."""
    test_list1: list[int] = [1,2,3,4,5,6,7,8,9]
    test_list2: list[int] = [1,2]
    assert concat(test_list1,test_list2) == [1,2,3,4,5,6,7,8,9,1,2]

def test_concat_empty_list() -> None:
    """Tests that concat works correctly when one list is empty. edge case."""
    test_list1: list[int] = [1,2,3,4,5]
    test_list2: list[int] = []
    assert concat(test_list1,test_list2) == [1,2,3,4,5]


def test_sub_ind1_neg() -> None:
    """"Tests that sub still works when ind1 is negative. edge case."""
    test_list: list[int] = [1,2,3,4,5,6,7]
    ind1: int = -4
    ind2: int = 6
    assert sub(test_list, ind1, ind2) == [1,2,3,4,5,6]

def test_sub_short_list() -> None:
    """Tests that sub works as expected"""
    test_list: list[int] = [1,2,3]
    ind1: int = 0
    ind2: int = 3
    assert sub(test_list, ind1, ind2) == [1,2,3]

def test_sub_small_difference_ind() -> None:
    """Tests that sub still works when the provided indexes are very close together."""
    test_list: list[int] = [1,2,3,4,5,6,7]
    ind1: int = 2
    ind2: int = 3
    assert sub(test_list, ind1, ind2) == [3]
