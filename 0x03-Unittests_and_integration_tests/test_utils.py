#!/usr/bin/python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Any


class TestAccessNestedMap(unittest.TestCase):
    """Test class that inherits from unittest.TestCase."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, result):
        """Unit test for utils.access_nested_map."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
