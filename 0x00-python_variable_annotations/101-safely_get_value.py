#!/usr/bin/env python3
"""
Apply proper annotaion to a function
"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
            dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
    Args:
        dct (Mapping like a dictionary)
        key (Any type)
        default (Any or None type)
    Return:
        (Any or None type)
    """
    if key in dct:
        return dct[key]
    else:
        return default
