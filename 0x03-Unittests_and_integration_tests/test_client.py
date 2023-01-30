#!/usr/bin/env python3
"""
Tests for GithubOrgClient class methods
"""
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import PropertyMock
from parameterized import parameterized
from typing import Dict, List

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

    def test_public_repos_url(self) -> None:
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

    @parameterized.expand([
        ('nginx-1.0', []),
        ('apache-2.0', ['dagger']),
        ('bsl-1.0', ['cpp-netlib', 'dot-net']),
    ])
    @patch('client.get_json')
    def test_public_repos(self, license_key: str,
                          expected: List[str], mockGetJson) -> None:
        """
        Test public_repos method
        Args:
            license_key (str): license key to validate
            expected (List): list of repo names with license_key
        Returns:
            None
        """
        config = {'return_value':
                  [{'name': 'cpp-netlib', 'license': {'key': 'bsl-1.0'}},
                   {'name': 'dagger', 'license': {'key': 'apache-2.0'}},
                   {'name': 'dot-net', 'license': {'key': 'bsl-1.0'}}]}
        mockGetJson.configure_mock(**config)
        propValue = {'return_value':
                     {'repos_url': 'https://api.github.com/orgs/google/repos'}}
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock, **propValue) as mockPublicRepo:
            test = GithubOrgClient('google')
            self.assertListEqual(test.public_repos(license_key), expected)
            mockPublicRepo.assert_called_once()
            mockGetJson.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, license: Dict,
                         key: str, expected: bool) -> None:
        """
        Test license check method
        Args:
            license (Dict): dictionary of license information
            key (str): license key
            expected (bool): `True` if key if valid else `False`
        Returns:
            bool
        """
        self.assertEqual(GithubOrgClient.has_license(license, key), expected)
