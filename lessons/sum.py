"""Summing the elements of a list using different loops."""

__author__: str = "730655689"


def w_sum(vals: list[float]) -> float:
    """Practice with while loops."""
    count: int = 0
    sum: float = 0
    while count < len(vals):
        sum += vals[count]
        count += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Practice with for loops."""
    sum: float = 0
    for num in vals:
        sum += num
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Practice with for loops."""
    sum: float = 0
    for int in range(len(vals)):
        sum += vals[int]
    return sum