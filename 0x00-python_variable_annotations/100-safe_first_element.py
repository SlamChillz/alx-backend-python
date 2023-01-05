#!/usr/bin/env python3
"""
Defines a duck type for first element of a sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
        lst (Sequence object)
    Returns
        The value of the first element in lst of None if list is empty
    """
    if lst:
        return lst[0]
    else:
        return None
