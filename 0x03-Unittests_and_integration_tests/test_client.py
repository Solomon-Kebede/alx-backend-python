#!/usr/bin/env python3

'''
Test for client.GithubOrgClient
'''

import unittest
from parameterized import parameterized
# from utils import access_nested_map
from client import get_json
from unittest.mock import MagicMock, patch
# from utils import memoize
from client import GithubOrgClient

from unittest.mock import create_autospec


class TestGithubOrgClient(unittest.TestCase):
    '''Testsuite for client.GithubOrgClient'''
    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Testcase for client.GithubOrgClient.org'''
        mock_response = MagicMock()
        mock_response.return_value = {}
        mock_get_json.return_value = mock_response
        org_url = f"https://api.github.com/orgs/{org_name}"
        instance = GithubOrgClient(org_name)
        instance.org()
        mock_get_json.assert_called_once_with(org_url)


if __name__ == '__main__':
    unittest.main()
