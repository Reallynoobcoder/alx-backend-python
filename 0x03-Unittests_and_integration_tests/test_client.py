from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
import unittest
from client import GithubOrgClient
from typing import Any, Dict


class TestGithubOrgClient(unittest.TestCase):
    """Defines a test case class for testing GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock) -> None:
        """Test org method of GithubOrgClient"""
        client = GithubOrgClient(org_name)

        mock_get_json.return_value = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(
            result, {
                "repos_url": f"https://api.github.com/orgs/{org_name}/repos"})
