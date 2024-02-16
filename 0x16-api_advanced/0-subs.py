#!/usr/bin/python3
"""Querry reddit API"""

import requests
"""importing requests module and argv"""


def number_of_subscribers(subreddit):
    """
    a function that takes one argument:
        subreddit
    and return the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # header file to prevent many request errors
    headers = {"User-Agent": "My user Agent 1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        count = data.get('subscribers', 0)
        return count
    else:
        return 0
