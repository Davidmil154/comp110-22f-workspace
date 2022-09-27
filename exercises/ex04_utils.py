"""EX04 - List Utilities."""


__author__ = "730622383"


def all(test_list: list[int], test_int: int) -> bool:
    """Determines weather or not every element of the list is the same as the provided int."""
    i: int = 0
    if len(test_list) == 0:
        return (False)
    while i < len(test_list):
        if test_list[i] != test_int:
            return (False)
        i += 1
    return (True)


def max(test_list: list[int]) -> int:
    """Determines the maximum number in a provided list of ints."""
    i: int = 0
    holder: int = test_list[0]
    if len(test_list) == 0:
        raise ValueError("max() arg is an empty list")
    while i < len(test_list):
        if test_list[i] > holder:
            holder = test_list[i]
            i += 1
        else:
            i += 1
    return (holder)


def is_equal(test_list_1: list[int], test_list_2: list[int]) -> bool:
    """Determines weather or not two lists are exactly equal."""
    if len(test_list_1) != len(test_list_2):
        return (False)
    i: int = 0
    while i < len(test_list_1):
        if test_list_1[i] != test_list_2[i]:
            return (False)
        i += 1
    return (True)