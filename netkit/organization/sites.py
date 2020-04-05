"""
Sites is a base class which collects data relating to sites registered in Netkit
"""
# Standard Library
from datetime import datetime
from typing import List, Union

# Third Party
import requests
from pytz import timezone

# First Party
from netkit.auth import Auth
from netkit.helpers.api import netbox_api
from netkit.helpers.exceptions import NetkitError


class Sites:
    """
    :param auth: Auth object used for authenting to the API
    """

    def __init__(self, auth: Auth):
        self._auth = auth
        self._sites = None

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

    def _get_sites(self) -> requests.Response:
        if self._sites is not None:
            return self._sites
        result = netbox_api(self._auth, "/api/dcim/sites")
        self._sites = result.json()['results']
        return self._sites

    @property
    def list_sites(self) -> List['SiteInfo']:
        """
        A list of [SiteInfo] objects representing sites
        """
        return [SiteInfo(site) for site in self._get_sites()]

    def create_site(self, **kwargs) -> 'SiteInfo':
        """
        Creates a new site with supplied arguments.
        Please see https://netbox.readthedocs.io/en/stable/api/examples/ for an exmaple payload
        """
        try:
            result = netbox_api(self._auth, "/api/dcim/sites/", payload=kwargs, method="POST")
            return SiteInfo(result.json())
        except Exception as error:
            raise NetkitError(message=error)


class SiteInfo:
    """
    Object representing a site
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
        The ID of the registered site
        """
        return self._attributes.get('id')

    @property
    def name(self) -> str:
        """
        The name of the registered site
        """
        return self._attributes.get('name')

    @property
    def slug(self) -> str:
        """
        The slug associated with the registered site
        """
        return self._attributes.get('slug')

    @property
    def status(self) -> dict:
        """
        The status of the site
        """
        return self._attributes.get('status')

    @property
    def region(self) -> Union[dict, None]:
        """
        The region the site resides in
        """
        return self._attributes.get('region')

    @property
    def tenant(self) -> Union[dict, None]:
        """
        The tenant the side resides in
        """
        return self._attributes.get('tenant')

    @property
    def facility(self) -> str:
        """
        The facility the site resides in
        """
        return self._attributes.get('facility')

    @property
    def asn(self) -> Union[int, None]:
        """
        The autonomous system number associated with the site
        """
        return self._attributes.get('asn')

    @property
    def time_zone(self) -> Union[timezone, None]:
        """
        The time zone of the site
        """
        if self._attributes.get('time_zone'):
            return timezone(self._attributes.get('time_zone'))
        return None

    @property
    def description(self) -> str:
        """
        The description for the site
        """
        return self._attributes.get('description')

    @property
    def physical_address(self) -> str:
        """
        The physical address of the site
        """
        return self._attributes.get('physical_address')

    @property
    def shipping_address(self) -> str:
        """
        The shipping address for the site
        """
        return self._attributes.get('shipping_address')

    @property
    def latitude(self) -> Union[int, None]:
        """
        The latitude of the site
        """
        return self._attributes.get('latitude')

    @property
    def longitude(self) -> Union[int, None]:
        """
        The longitude of the site
        """
        return self._attributes.get('longitude')

    @property
    def contact_name(self) -> str:
        """
        The contact name for the site
        """
        return self._attributes.get('contact_name')

    @property
    def contact_phone(self) -> str:
        """
        The contact phone number for the site
        """
        return self._attributes.get('contact_phone')

    @property
    def contact_email(self) -> str:
        """
        The email address of the site contact
        """
        return self._attributes.get('contact_email')

    @property
    def comments(self) -> str:
        """
        Comments related to the site
        """
        return self._attributes.get('comments')

    @property
    def tags(self) -> list:
        """
        Any tags related to the site
        """
        return self._attributes.get('tags')

    @property
    def custom_fields(self) -> dict:
        """
        Any custom fields related to the site
        """
        return self._attributes.get('custom_fields')

    @property
    def created(self) -> datetime:
        """
        The date the site was created
        """
        created_date = datetime.strptime(self._attributes.get('created'), '%Y-%m-%d')
        return created_date

    @property
    def last_updated(self) -> datetime:
        """
        The date and time the site was last updated
        """
        updated_time = datetime.strptime(
            self._attributes.get('last_updated'), "%Y-%m-%dT%H:%M:%S.%fZ"
        )
        return updated_time

    @property
    def circuit_count(self) -> Union[int, None]:
        """
        The circuit count for the site
        """
        return self._attributes.get('circuit_count')

    @property
    def device_count(self) -> Union[int, None]:
        """
        The device count for the site
        """
        return self._attributes.get('device_count')

    @property
    def prefix_count(self) -> Union[int, None]:
        """
        The prefix count for the site
        """
        return self._attributes.get('prefix_count')

    @property
    def rack_count(self) -> Union[int, None]:
        """
        The rack count for the site
        """
        return self._attributes.get('rack_count')

    @property
    def virtualmachine_count(self) -> Union[int, None]:
        """
        The virtual machine count for the site
        """
        return self._attributes.get('virtualmachine_count')

    @property
    def vlan_count(self) -> Union[int, None]:
        """
        The VLAN count for the site
        """
        return self._attributes.get('vlan_count')
