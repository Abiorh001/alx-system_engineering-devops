#!/usr/bin/env python3
""" a script to list an employee task from json api"""
import requests
import sys
if __name__ == "__main__":
    id = sys.argv[1]
    url_id = "https://jsonplaceholder.typicode.com/users/" + id
    response = requests.get(url_id).json()
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + id
    new_response = requests.get(url_todo).json()

    total_items = 0
    completedtask = []

    for todo in new_response:
        if todo['userId'] == int(id):
            total_items += 1
            if todo['completed']:
                completedtask.append(todo['title'])
    print("Employee {} is done with tasks ({}/{}):"
          .format(response['name'], len(completedtask), total_items))
    for task_completed in completedtask:
        print("\t{}".format(task_completed))
