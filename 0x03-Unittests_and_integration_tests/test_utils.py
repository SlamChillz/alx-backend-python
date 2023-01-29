#!/usr/bin/env python3
"""
Tests for utils.py module
"""
import unittest
from parameterized import parameterized
from typing import (
    Dict, Tuple, Union
)
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Defines method to test nested map access
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[int, Dict]):
        """
        Test access to nested map
        Args:
            nested_map (Dict): nested dictionary
            path (Tuple): tuple of possible dictionary keys
            expected (int | Dict): expected result of tested function
        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Union[int, Dict]):
        """
        Test if an exception is correctly raised
        Args:
            same as described above
        Returns:
            None
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
