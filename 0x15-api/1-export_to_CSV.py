#!/usr/bin/python3
"""Fetching JSON data from an API and dumping to CSV."""

import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_response = requests.get(url).json()
    user_name = user_response.get("username")
    todo_response = requests.get(url + "/todos").json()
    file_name = user_id + ".csv"

    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for item in todo_response:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                item.get("userId"), user_name, item.get("completed"), item.get("title")))
