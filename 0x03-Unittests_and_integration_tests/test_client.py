#!/usr/bin/env python3
"""
Tests for GithubOrgClient class methods
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Defines test for Github Org Client
    """
    @parameterized.expand(["google", "abc"])
    @patch('client.get_json')
    def test_org(self, org: str, getJson: MagicMock) -> None:
        """
        Tests the org property of GithubOrgClient class
        Args:
            org (str): organization
            getJson (MagicMock): a MagicMock object of `get_json` funtion
        Returns:
            None
        """
        gitClient = GithubOrgClient(org)
        self.assertEqual(gitClient.org, getJson.return_value)
        getJson.assert_called_once_with(gitClient.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """
        Test _public_repos_url property
        """
        config = {'return_value':
                  {'repos_url': 'https://api.github.com/slam/repos/alx'}}

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock, **config) as mockOrg:
            test = GithubOrgClient('alx')
            self.assertEqual(test._public_repos_url,
                             mockOrg.return_value['repos_url'])
