"""EX07 - Dict Functions."""


__author__ = "730622383"


def invert(test_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key value pairs of a dict."""
    returner: dict[str, str] = {}
    for value in test_dict:
        for item in returner:
            if item == test_dict[value]:
                raise KeyError("KeyError, you tried to make a dict with two of the same key")
        returner[test_dict[value]] = value
        print(returner)
    return (returner)


def count(list: list[str]) -> dict[str, int]:
    """Counts the amount of times a value appears in a list and returns a dict."""
    returner: dict[str, int] = {}
    for item in list:
        if item in returner:
            returner[item] += 1
        else:
            returner[item] = 1
    return (returner)


def favorite_color(given: dict[str, str]) -> str:
    """Takes in person name and favorite color, returns most frequent favorite color."""
    color_list: list[str] = []
    counter: dict[str, int] = {}
    for value in given:
        color_list.append(given[value])
    for item in color_list:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
    holder: int = 0
    xt: str = ""
    for unit in counter:
        if counter[unit] > holder:
            holder = counter[unit]
            xt = unit
    return (xt)