"""Example four."""

__author__: str = "730655689"


def all(x: list[int], y: int) -> bool:
    """Returns True if y matches all integers in x."""
    tf: bool = True
    count: int = 0
    if len(x) == 0:
        return False
    while count < len(x):
        if x[count] != y:
            tf = False
        count += 1
    return tf


def max(x: list[int]) -> int:
    """Returns the highest int in the given list."""
    if len(x) == 0:
        raise ValueError("max() arg is an empty List")
    set: int = x[0]
    count: int = 0
    while count < len(x):
        if x[count] > set:
            set = x[count]
        count += 1
    return set


def is_equal(x: list[int], y: list[int]) -> bool:
    """Returns True is two lists are exactly equal."""
    if len(x) != len(y):
        return False
    count: int = 0
    check: bool = True
    while count < len(x):
        if x[count] != y[count]:
            check = False
        count += 1
    return check
