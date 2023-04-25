#!/usr/bin/python3
"""Fetching JSON data from an API and dumping to json."""

import json
import sys
import requests


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(url).json()
    user_name = user_response.get("username")
    todo_response = requests.get(url + "/todos").json()
    file_name = user_id + ".json"
    my_dict = {}

    my_dict[user_id] = []

    for item in todo_response:
        inner_dict = {}
        inner_dict["task"] = item.get("title")
        inner_dict["completed"] = item.get("completed")
        inner_dict["username"] = user_name
        my_dict.get(user_id).append(inner_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
