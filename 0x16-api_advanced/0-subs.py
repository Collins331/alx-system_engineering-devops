#!/usr/bin/python3
"""
import requests module
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the subscribers of a subreddit

    Args:
        subreddit (_type_): _description_
    Return:
        the number of subscribers in a subredit or 0 if it doesn't exit
    """
    # Base URL for the subreddit information endpoint
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set a custom User-Agent header to avoid throttling
    headers = {"User-Agent": "My user Agent 1.0"}

    try:
        # Send a GET request without following redirects
        response = requests.get(url, allow_redirects=False, headers=headers)

        # Check for successful response
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract and return the subscriber count
            return data.get("data", {}).get("subscribers", 0)
        else:
            # Handle unsuccessful response, assuming invalid subreddit
            return 0

    except requests.exceptions.RequestException as e:
        # Handle any other errors during the request
        return 0
