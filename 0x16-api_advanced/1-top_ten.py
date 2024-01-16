#!/usr/bin/python3
"""
Module that queries the REDDIT API to get top 10 subreddits
"""
from requests import get


def top_ten(subreddit):
    """
    This is a function that queries the REDDIT API to get the first 10
    posts listed in a subreddits
    """
    if subreddit is None or type(subreddit) is not str:
        print("None")

    user_agent = {'User-Agent': '0x16.api_advanced:Google Chrome(Linux)'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    resp = get(url, headers=user_agent, allow_redirects=False)

    if resp.status_code == 404:
        print("None")
    else:
        for item in resp.json().get('data').get('children'):
            print(item.get('data').get('title'))
