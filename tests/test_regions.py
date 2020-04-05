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
from netkit.organization.regions import Regions


def fake_api(*args, **kwargs):
    """
    Creates the fake api result for mocking later
    """
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "assets/regions/regions_list.json"))
    with open(filepath, "r") as fp:
        return json.load(fp)


class NetkitRegionsTest(unittest.TestCase):
    """
    A collection of tests to check the Netkit.organization.regions.Regions class
    """

    def __init__(self, *args, **kwargs):
        super(NetkitRegionsTest, self).__init__(*args, **kwargs)

    @requests_mock.mock()
    def test_regions_properties(self, mock_requests):
        """
        Tests the properties returned by the Netkit.organization.region.Regions class by mocking
        against an asset file containing a valid JSON response
        """
        mock_requests.register_uri(
            "GET", "https://netkit.example.com/api/dcim/regions", json=fake_api
        )

        auth = Auth(token='foo', url='https://netkit.example.com')
        regions = Regions(auth)
        region_one = regions.list_regions[0]
        self.assertEqual(region_one.id, 1)
        self.assertIsInstance(region_one.id, int)
        self.assertEqual(region_one.name, 'United Kingdom')
        self.assertEqual(region_one.slug, 'united-kingdom')
        self.assertIsNone(region_one.parent)
        self.assertEqual(region_one.site_count, 1)
