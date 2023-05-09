#!/usr/bin/python3
"""a script to fetch api recursively"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """a functiion to perform an api recursively"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'chrome'}
    global after
    params = {"after": after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data").get("children")
        next_ = data.get("data").get("after")
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        for post in posts:
            hot_list.append(post['data']['title'])
        return hot_list
    else:
        return (None)
