#!/usr/bin/env python3
"""
Defines a function called 'make_multiplier'
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        k (str)
        v (int or float)
    Return:
        (tuple): a tuple of k and square of v
    """
    def multiply(f: float) -> float:
        """
        Multiplies multiplier by f
        Args:
            f (float)
        Returns:
            (float)
        """
        return multiplier * f
    return multiply
