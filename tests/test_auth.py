"""
Tests Netkit.Auth Class
"""
# Standard Library
import json
import unittest
from os import path

# Third Party
import requests_mock

# First Party
from netkit.auth import Auth


def fake_api(*args, **kwargs):
    """
    Creates the fake api result for mocking later
    """
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "assets/sites/sites_list.json"))
    with open(filepath, "r") as fp:
        return json.load(fp)


class NetkitAuthTest(unittest.TestCase):
    """
    A collection of tests to check the Netkit.Auth class
    """

    def __init__(self, *args, **kwargs):
        super(NetkitAuthTest, self).__init__(*args, **kwargs)

    @requests_mock.mock()
    def test_auth(self, mock_requests):
        """
        Tests the properties returned by the Netkit.Auth class by mocking
        against an asset file containing a valid JSON response
        """
        mock_requests.register_uri(
            "GET", "https://netkit.example.com/api/dcim/sites", json=fake_api
        )

        auth = Auth(token='foo', url='https://netkit.example.com')
        self.assertEqual(auth.token, 'foo')
        self.assertEqual(auth.url, 'https://netkit.example.com')
        self.assertTrue(auth.is_valid())
