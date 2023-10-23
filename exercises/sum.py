"""Summing the elements of a list using different loops."""

__author__: str = "730655689"


def w_sum(vals: list[float])-> float:
    """practice with while loops."""
    count:int=0
    sum:int=0
    while count<len(vals):
        sum+=vals[count]
    return sum


def f_sum(vals: list[float])-> float:
    """practice with for loops."""
    sum:int=0
    for int in vals:
        sum+=int
    return sum


def f_range_sum(vals: list[float])-> float:
    """practice with for loops."""
    sum:int=0
    for int in range(len(vals)):
        sum+=vals[int]
    return sum

