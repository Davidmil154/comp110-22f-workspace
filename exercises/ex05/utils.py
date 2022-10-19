"""EX05 - List Utility Functions."""


__author__ = "730622383"


def only_evens(given: list[int]) -> list[int]:
    """Returns a list containing only the even numbers of the provided list."""
    returner: list[int] = []
    for num in given:
        if num % 2 == 0:
            returner.append(num)
    return returner


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns a new list, containing the first list followed by the second list."""
    returner: list[int] = []
    for num in first:
        returner.append(num)
    for num in second:
        returner.append(num)
    return returner


def sub(givenL: list[int], ind1: int, ind2: int) -> list[int]:
    """Takes a list and two ints(for indexes), and returns a new list of all the values between the ints."""
    returner: list[int] = []
    if ind1 < 0:
        i = 0
    else:
        i = ind1
    if ind2 > len(givenL):
        ind2 = len(givenL)
    while i < ind2:
        returner.append(givenL[i])
        i = i + 1
    return returner