#!/usr/bin/env python3
"""Fetching JSON data from an API and dumping to CSV."""

import csv
import sys
import requests


if __name__ == "__main__":
    employee_user_id = sys.argv[1]
    url_for_users = "https://jsonplaceholder.typicode.com/users/{}".format(employee_user_id)
    user_response = requests.get(url_for_users).json()
    user_name = user_response.get("username")
    todo_response = requests.get(url_for_users + "/todos").json()
    file_name = employee_user_id + ".csv"

    with open(file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for item in todo_response:
             csvfile.write('"{}","{}","{}","{}"\n'.format(item.get(
                "userId"), user_name, item.get("completed"),
                item.get("title")))

