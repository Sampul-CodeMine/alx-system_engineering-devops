#!/usr/bin/python3
"""
This is a module that uses the get HTTP header method to get resources
from the Reddit API
"""
import json
import requests


def count_words(subreddit, word_list, count=[], after=""):
    """
    This is a function that count words using the REDDIT API
    """
    ua = {
          'User-Agent': 'Google Chrome Version 115.0.0.0:v1.0.0 (by /u/bdov_)'
          }
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    if after == "" or after is None:
        count = len(word_list) * [0]

    params = {'after': after}
    resp = requests.get(url, headers=ua, allow_redirects=False, params=params)
    if resp.status_code == 200:
        data = resp.json()

        for heading in (data['data']['children']):
            for word in heading['data']['title'].split():
                for item in range(len(word_list)):
                    if word_list[item].lower() == word.lower():
                        count[item] += 1
        after = data['data']['after']
        if after is None:
            keep = []
            for itr in range(len(word_list)):
                for tmp in range(itr + 1, len(word_list)):
                    if word_list[itr].lower() == word_list[tmp].lower():
                        keep.append(tmp)
                        count[itr] += count[tmp]

            for itr in range(len(word_list)):
                for tmp in range(itr, len(word_list)):
                    if (count[tmp] > count[itr] or
                            (word_list[itr] > word_list[tmp] and
                             count[tmp] == count[itr])):
                        aux = count[itr]
                        count[itr] = count[tmp]
                        count[tmp] = aux
                        aux = word_list[itr]
                        word_list[itr] = word_list[tmp]
                        word_list[tmp] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in keep:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, count, after)
