import requests
from furl import furl


def verify(secret, response, remoteip=None, endpoint=None):
    """
    Verify a Google reCAPTCHA 2.0 response.
    """

    if endpoint is None:
        endpoint = "https://www.google.com/recaptcha/api/siteverify"

    query = furl(endpoint)
    query.args['secret'] = secret
    query.args['response'] = response
    if remoteip:
        query.args['remoteip'] = remoteip

    response = requests.get(query.url)
    result = response.json()

    return result
