#!/usr/bin/env python3
"""Parameterize a unit test."""
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
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str],
        expected_result: Any
    ) -> None:
        """Unit test for utils.access_nested_map."""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map(self, nested_map: Dict[str, Any],
                               path: Tuple[str], expected_result: Any):
        """assertRaises test for utils.access_nested_map."""
        with self.assertRaises(expected_result):
            access_nested_map(nested_map, path)
