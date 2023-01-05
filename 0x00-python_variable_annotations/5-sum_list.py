#!/usr/bin/env python3
"""
Defines a function called 'sum_list'
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of float numbers
    Args:
        input_list (list): a list of floats
    Return:
        (float)
    """
    return sum(input_list)
