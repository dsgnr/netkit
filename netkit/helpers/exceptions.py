"""
Custom exceptions for Netkit
"""
# Standard Library
from typing import Dict


class NetkitError(Exception):
    """ An exception handler for all exceptions
    :param message: A defined error message placed within the exception
    """

    def __init__(self, *, message=None):
        super(NetkitError, self).__init__(message)
        self._message = message or "Something went wrong"

    def __repr__(self):
        attrs = {
            "cls": self.__class__.__name__,
            "at": hex(id(self)),
            "message": self._message,
        }
        return "<{cls}: (at {at}) message={message!r}>".format(**attrs)

    @property
    def message(self) -> str:
        """
        The error message describing why the exception was raised.
        """
        return self._message

    def as_json(self) -> Dict:
        """
        The error represented as a JSON dictionary
        """
        return {"error": True, "message": self.message}
