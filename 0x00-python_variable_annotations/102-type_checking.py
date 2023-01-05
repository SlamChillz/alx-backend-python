#!/usr/bin/env python3
"""
Type checking with mypy
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Increase elements of an array by doubling each element in the given array
    Args:
        lst (Sequence -> Tuple)
        factor (int): Factor of increase
    Return:
        (List): list of the zoomed array
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
