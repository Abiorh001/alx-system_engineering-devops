#!/usr/bin/python3
""" a script to fecth top ten post"""

import requests


def top_ten(subreddit):
    """ a function to perform the task """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {"User-Agent": "Chrome"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    data = response.json()

    if response.status_code == 200:
        posts = data.get("data").get("children")
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
