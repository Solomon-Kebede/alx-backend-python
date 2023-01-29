#!/usr/bin/env python3

'''
TestAccessNestedMap
'''

import unittest
from utils import access_nested_map
from parameterized import parameterized


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


if __name__ == '__main__':
    unittest.main()
