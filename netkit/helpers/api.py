"""
Helper to interact with the NetBox API
"""
# Third Party
import requests


def netbox_api(
    auth: 'Auth', path: str, payload: dict = None, method: str = "GET"
) -> requests.Response:
    """
    :param auth: Auth object to use for authentication to the API
    :param path: The NetBox API endpoint to use
    :param payload: The data sent to the API
    :param method: The request type
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
    except Exception as error:
        raise Exception(f"Invalid response received from NetBox API when retrieving data: {error}")
