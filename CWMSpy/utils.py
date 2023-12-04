import requests


def queryCDA(url, payload, headerList):
    """Send a query.

    Wrapper for requests.get that handles errors and returns response.

    Parameters
    ----------
    url: string
        URL to query
    payload: dict
        query parameters passed to ``requests.get``

    Returns
    -------
    string: query response
        The response from the API query ``requests.get`` function call.
    """


    response = requests.get(url, params=payload, headers=headerList)

    if response.status_code == 400:
        raise ValueError(
            f'Bad Request, check that your parameters are correct. URL: {response.url}'
        )
    elif response.status_code == 404:
        raise ValueError(
            'Page Not Found Error. May be the result of an empty query. '
            + f'URL: {response.url}'
        )
    return response