"""
Helper to interact with the NetBox API
"""
import requests


def netbox_api(auth, path, payload=None, method="GET"):
    """
    :param auth: Auth object to use for authentication to the API
    :type auth: Auth
    :param path: The NetBox API endpoint to use
    :type path: str
    :param payload: The data sent to the API
    :type payload: dict
    :param method: The request type
    :type method: str
    :returns: The NetBox API response object
    :rtype: dict

    :raises Exception: Catches all exceptions
    """
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Token {auth.token}",
    }
    if method not in ["GET", "POST", "PUT"]:
        raise ValueError("Method must be either GET, POST or PUT")
    try:
        url = auth.url + path
        response = requests.request(method, url, json=payload, headers=headers)
        response.raise_for_status()
        return response
    except Exception as ex:
        raise Exception(f"Invalid response received from NetBox API when retrieving data: {ex}")
