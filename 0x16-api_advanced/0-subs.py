#!/usr/bin/python3
"""
This is a module that uses the get HTTP header method to get resources
from the Reddit API
"""
from requests import get


def number_of_subscribers(subreddit):
    """
    This is a function that gets the number of total subscribers for a given
    subreddit using the REDDIT API
    """
    if subreddit is None or type(subreddit) is not str:
        return 0

    user_agent = {'User-Agent': '0x16.api_advanced:Google Chrome(Linux)'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    resp = get(url, headers=user_agent, allow_redirects=False)
    status = resp.status_code
    try:
        if status == 404:
            return 0
        else:
            return resp.json().get('data').get('subscribers')
    except (Exception):
        return 0
