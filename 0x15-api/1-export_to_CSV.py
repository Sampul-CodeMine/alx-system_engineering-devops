#!/usr/bin/python3
"""
This is a function that exports data from an API to
a flat file in csv format
"""

if __name__ == "__main__":

    import csv
    import requests as rq
    import sys

    uid = sys.argv[1]
    user = rq.get("https://jsonplaceholder.typicode.com/users/{}".format(uid))
    name = user.json().get('username')
    todos = rq.get('https://jsonplaceholder.typicode.com/todos')

    fn = uid + '.csv'
    with open(fn, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(uid):
                writer.writerow([uid, name, str(task.get('completed')),
                                task.get('title')])
