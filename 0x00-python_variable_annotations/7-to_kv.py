#!/usr/bin/env python3
"""
Defines a function called 'to_kv'
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k (str)
        v (int or float)
    Return:
        (tuple): a tuple of k and square of v
    """
    return k, v*v
