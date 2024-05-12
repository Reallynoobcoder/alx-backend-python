#!/usr/bin/env python3
"""Parameterize a unit test."""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Dict, Tuple, Any
from unittest.mock import patch, Mock


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

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """test access_nested_map function for exceptions"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test case class for testing the 'get_json' function."""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch('requests.get')
    def test_get_json(self,
                      url_test: str,
                      payload_test: Dict[str, bool],
                      mock_get: Mock):
        """Mock test the method utils.get_json."""
        mock_get.return_value = Mock()

        mock_get.return_value.json.return_value = payload_test

        result = get_json(url_test)

        mock_get.assert_called_once_with(url_test)

        self.assertEqual(result, payload_test)


class TestMemoize(unittest.TestCase):
    """Test case class for testing memoization."""

    def test_memoize(self):
        """Test memoization by mocking a_method and checking property calls"""
        class TestClass:
            """doc doc doc"""

            def a_method(self) -> int:
                """mock a_method."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Cheking property."""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            test_obj = TestClass()
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            mock_method.assert_called_once()

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
