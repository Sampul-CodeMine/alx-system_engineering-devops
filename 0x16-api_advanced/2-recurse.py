#!/usr/bin/python3
"""
This is a module that uses the get HTTP header method to get resources
from the Reddit API
"""
from requests import get


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    This is a function that recursively returns the 10 top post from a
    subreddit using the REDDIT API
    """
    if subreddit is None or type(subreddit) is not str:
        return None
    user_agent = {'User-Agent': 'Google Chrome Version 115.0.0.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after, 'count': count, 'limit': 100}
    resp = get(url, headers=user_agent, allow_redirects=False, params=params)

    if resp.status_code == 404:
        return None
    
    data = resp.json().get('data')
    after = data.get('after')
    count += data.get('dist')

    for title in data.get('children'):
        hot_list.append(title.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
