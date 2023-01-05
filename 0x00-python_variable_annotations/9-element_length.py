#!/usr/bin/env python3
"""
Defines a duck typed iterable object
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable of Sequence)
    Returns:
        List of Tuples
    """
    return [(i, len(i)) for i in lst]
