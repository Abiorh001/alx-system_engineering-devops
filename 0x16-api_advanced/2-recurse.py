#!/usr/bin/python3
"""a script to fetch api recursively"""

import requests


def recurse(subreddit, hot_list=[]):
    """a function to perform an api recursively"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {'User-Agent': 'chrome'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()
        posts = data.get("data").get("children")

        for post in posts:
            hot_list.append(post['data']['title'])

        if posts['data']['after'] is not None:
            recurse(subreddit, hot_list=hot_list)
        return hot_list
    else:
        return None
