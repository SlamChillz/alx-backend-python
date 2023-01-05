#!/usr/bin/env python3
"""
Defines a function called 'sum_mixed_list'
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integer and float numbers
    Args:
        mxd_lst (list): a list of integers and floats
    Return:
        (float)
    """
    return sum(mxd_lst)
