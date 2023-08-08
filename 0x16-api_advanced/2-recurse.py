#!/usr/bin/python3
"""
This is a module that uses the get HTTP header method to get resources
from the Reddit API
"""
from requests import get


def recurse(subreddit, hot_list=[], count=0, after=""):
    """
    This is a function that recursively returns the 10 top post from a
    subreddit using the REDDIT API
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    user_agent = {'User-Agent': 'Google Chrome Version 115.0.0.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after, 'count': count}
    resp = get(url, headers=user_agent, allow_redirects=False, params=params)
    result = resp.json()

    if resp.status_code == 404:
        return None
    after = result.get('data').get('after')
    count = result.get('data').get('dist')
    for item in result.get('data').get('children'):
        hot_list.append(item.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, count, after)
    return hot_list
