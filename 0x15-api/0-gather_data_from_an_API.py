#!/usr/bin/python3
"""
A function that displays a list of TODO for a given employee
with the employee ID specified
"""


if __name__ == "__main__":
    import requests as rq
    import sys

    uid = sys.argv[1]
    user = rq.get("https://jsonplaceholder.typicode.com/users/{}".format(uid))

    name = user.json().get('name')

    todos = rq.get('https://jsonplaceholder.typicode.com/todos')
    totalTD = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(uid):
            totalTD += 1
            if task.get('completed'):
                completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTD))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(uid) and task.get('completed')]))
