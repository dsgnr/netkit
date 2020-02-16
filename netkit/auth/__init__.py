"""
Auth is a base object which passes through attributes such as the authentication token
and base url to subsequent requests.
"""
# Third Party
import requests

# First Party
from netkit.helpers.api import netbox_api


class Auth:
    """
    The Auth class is used to store various authentication parameters.
    An Auth object is required on all objects that interact with a NetBox instance API

    :param token: The authentication token
    :param url: The base url of the NetBox instance
    """

    def __init__(self, token: str, url: str):
        self._token = token
        self._url = url
        self._is_valid = False

    def __repr__(self):
        attrs = {
            "cls": self.__class__.__name__,
            "at": hex(id(self)),
            "token": bool(self._token),
            "url": self._url,
            "is_valid": self._is_valid,
        }
        return "<{cls}: (at {at}) token={token!r} url={url!r} is_valid={is_valid!r}>".format(
            **attrs
        )

    @property
    def token(self) -> str:
        """
        Returns the token passed into the object

        """
        return self._token or None

    @property
    def url(self) -> str:
        """
        Returns the base url of the Netbox instance

        """
        return self._url or None

    def is_valid(self) -> bool:
        """
        Attempts to establish a connection to the Netbox instance to verify the token provided

        """
        result = netbox_api(self, "/api/dcim/sites")
        self._is_valid = bool(result.status_code == 200)
        return self._is_valid
