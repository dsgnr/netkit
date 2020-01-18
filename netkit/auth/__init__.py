"""
Auth is a base object which passes through attributes such as the authentication token
and base url to subsequent requests.
"""
import requests

from netkit.helpers.api import netbox_api


class Auth():
    """
    The Auth class is used to store various authentication parameters.
    An Auth object is required on all objects that interact with a NetBox instance API

    :param token: The authentication token
    :type token: str
    :param base_url: The base url of the NetBox instance
    :type base_url: str
    """
    def __init__(self, token=None, base_url=None):
        self._token = token
        self._base_url = base_url
        self._is_valid = False

    def __repr__(self):
        attrs = {
            "cls": self.__class__.__name__,
            "at": hex(id(self)),
            "token": bool(self._token),
            "url": self._base_url,
            "is_valid": self._is_valid,
        }
        return "<{cls}: (at {at}) token={token!r} url={url!r} is_valid={is_valid!r}>".format(
            **attrs
        )

    @property
    def token(self):
        """
        Returns the token passed into the object

        :type: str
        """
        return self._token or None

    @property
    def url(self):
        """
        Returns the base url of the Netbox instance

        :type: str
        """
        return self._base_url or None

    def is_valid(self):
        """
        Attempts to establish a connection to the Netbox instance to verify the token provided

        :type: bool
        """
        result = netbox_api(self, "/api/dcim/sites",)
        self._is_valid = bool(result.status_code == 200)
        return self._is_valid
