"""
Tests Netkit.Sites Class
"""
# Standard Library
import json
import unittest
from os import path

# Third Party
import requests_mock

# First Party
from netkit.auth import Auth
from netkit.sites import Sites


def fake_api(*args, **kwargs):
    """
    Creates the fake api result for mocking later
    """
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "assets/sites/sites_list.json"))
    with open(filepath, "r") as fp:
        return json.load(fp)


class NetkitSitesTest(unittest.TestCase):
    """
    A collection of tests to check the Netkit.Sites class
    """

    def __init__(self, *args, **kwargs):
        super(NetkitSitesTest, self).__init__(*args, **kwargs)

    @requests_mock.mock()
    def test_sites_properties(self, mock_requests):
        """
        Tests the properties returned by the Netkit.Sites class by mocking
        against an asset file containing a valid JSON response
        """
        mock_requests.register_uri(
            "GET", "https://netkit.example.com/api/dcim/sites", json=fake_api
        )

        auth = Auth(token='foo', url='https://netkit.example.com')
        sites = Sites(auth)
        site_one = sites.list_sites[0]
        self.assertEqual(site_one.id, 1)
        self.assertIsInstance(site_one.id, int)
        self.assertEqual(site_one.name, 'Netkit Lab')
        self.assertEqual(site_one.slug, 'netkit-lab')
        self.assertEqual(site_one.status, {"value": 1, "label": "Active"})
        self.assertEqual(site_one.facility, 'Homelab')
        self.assertEqual(site_one.asn, 12200)
        self.assertIsInstance(site_one.asn, int)
        self.assertIsNone(site_one.latitude)
        self.assertIsNone(site_one.longitude)
        self.assertFalse(site_one.tags)
        self.assertIsNone(site_one.circuit_count)
        self.assertIsNone(site_one.vlan_count)
