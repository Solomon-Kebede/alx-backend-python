#!/usr/bin/env python3

'''
TestAccessNestedMap
'''

import unittest
from utils import access_nested_map
from parameterized import parameterized
from utils import get_json
from unittest.mock import MagicMock, patch
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    '''Testsuite for utils.access_nested_map'''
    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b")),
    ])
    def test_access_nested_map(self, nested_map, path):
        '''Testcase for utils.access_nested_map'''
        expected_result = nested_map
        for i in range(len(path)):
            expected_result = expected_result.get(path[i])
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Testcase for Exceptions in utils.access_nested_map'''
        expected_result = nested_map
        for i in range(len(path)):
            key = path[i]
            if key not in expected_result.keys():
                with self.assertRaises(KeyError):
                    expected_result = expected_result[key]


class TestGetJson(unittest.TestCase):
    '''Testsuite for utils.get_json'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_requests):
        '''Testcase for utils.get_json'''
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_requests.get.return_value = mock_response
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    '''Testsuite for utils.memoize'''
    def test_memoize(self):
        '''Testcase for utils.memoize'''
        class TestClass:
            '''TestClass class'''
            def a_method(self):
                '''Returns 42'''
                return 42

            @memoize
            def a_property(self):
                '''Property method'''
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
        ) as mock_method:
            instance = TestClass()
            instance.a_property
            instance.a_property
        mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
