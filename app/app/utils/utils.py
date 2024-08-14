from math import floor, ceil


def floor_decimal(number: float, decimals: int) -> float:
    helper = 10 ** decimals
    return floor(number * helper) / helper


def ceil_decimal(number: float, decimals: int) -> float:
    helper = 10 ** decimals
    return ceil(number * helper) / helper


def round_decimal(number: float, decimals: int) -> float:
    helper = 10 ** decimals
    return round(number * helper) / helper
