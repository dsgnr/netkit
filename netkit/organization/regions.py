"""
Region is a base class which collects data relating to a region registered in Netkit
"""
# Standard Library
from typing import List, Union

# Third Party
import requests

# First Party
from netkit.auth import Auth
from netkit.helpers.api import netbox_api


class Regions:
    """
    :param auth: Auth object used for authenting to the API
    """

    def __init__(self, auth: Auth):
        self._auth = auth
        self._regions = None

    def __repr__(self):
        attrs = {
            "cls": self.__class__.__name__,
            "at": hex(id(self)),
        }
        return "<{cls}: (at {at})>".format(**attrs)

    @property
    def auth(self) -> Auth:
        """
        The [Auth] object used to authenticate to the instance
        """
        return self._auth

    def _get_regions(self) -> requests.Response:
        if self._regions is not None:
            return self._regions
        result = netbox_api(self._auth, "/api/dcim/regions")
        self._regions = result.json()['results']
        return self._regions

    @property
    def list_regions(self) -> List['RegionInfo']:
        """
        A list of [RegionInfo] objects representing regions
        """
        try:
            return [RegionInfo(region) for region in self._get_regions()]
        except TypeError:
            return []


class RegionInfo:
    """
    Object representing a region
    """

    def __init__(self, attributes):
        self._attributes = attributes

    def __repr__(self):
        attrs = {
            "cls": self.__class__.__name__,
            "at": hex(id(self)),
            "id": self.id,
            "name": self.name,
        }
        return "<{cls}: (at {at}) id={id!r} name={name!r}>".format(**attrs)

    @property
    def id(self) -> int:
        """
        The ID of the registered region
        """
        return self._attributes.get('id')

    @property
    def name(self) -> str:
        """
        The name of the registered region
        """
        return self._attributes.get('name')

    @property
    def slug(self) -> str:
        """
        The slug associated with the registered region
        """
        return self._attributes.get('slug')

    @property
    def parent(self) -> str:
        """
        The parent of the region
        """
        return self._attributes.get('parent')

    @property
    def site_count(self) -> Union[int, None]:
        """
        The quantity of sites in the region
        """
        return self._attributes.get('site_count')
