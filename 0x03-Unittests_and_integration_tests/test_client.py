#!/usr/bin/env python3

'''
Test for client.GithubOrgClient
'''

import unittest
from parameterized import parameterized
from client import get_json
from unittest.mock import MagicMock, patch
# from utils import memoize
from client import GithubOrgClient

from unittest.mock import create_autospec
from unittest.mock import PropertyMock
from utils import access_nested_map


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

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    def test_public_repos_url(self, org_name):
        '''Testcase for client.GithubOrgClient._public_repos_url'''
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = {}
            instance = GithubOrgClient(org_name)
            self.assertEqual(GithubOrgClient._public_repos_url, {})

    @parameterized.expand([
        (
            'google',
            [
                {'name': 'truth'},
                {'name': 'ruby-openid-apps-discovery'},
                {'name': 'autoparse'},
            ],
            ['truth', 'ruby-openid-apps-discovery', 'autoparse',]
        ),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, json_res, repos_list, mock_get_json):
        '''Testcase for client.GithubOrgClient.public_repos'''
        mock_get_json.return_value = json_res  # patch get_json
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = json_res
            instance = GithubOrgClient(org_name)
            '''Test that the repo list is what you expect
            from the chosen payload'''
            self.assertEqual(instance.public_repos(None), repos_list)
        # Test that the mocked property and the mocked get_json was called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, boolen_return):
        '''Testcase for client.GithubOrgClient.has_license'''
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), boolen_return
        )

class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Test the GithubOrgClient.public_repos method in an integration test'''
    pass

if __name__ == '__main__':
    unittest.main()
