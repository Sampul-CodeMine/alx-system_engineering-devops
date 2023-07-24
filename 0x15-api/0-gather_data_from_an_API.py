#!/usr/bin/python3
"""
A function that displays a list of TODO for a given employee
with the employee ID specified
"""


if __name__ == "__main__":
    import requests as rq
    import sys

    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = rq.get("{}users/{}".format(url, uid))

    name = user.json().get('name')

    todos = rq.get('{}users/{}/todos'.format(url, uid))
    tasks = todos.json()
    totalTD = []
    completed = 0

    for task in tasks:
        if task.get('completed'):
            totalTD.append(task)
            completed += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, len(tasks)))

    for task in totalTD:
        print("\t{}".format(task.get('title')))
