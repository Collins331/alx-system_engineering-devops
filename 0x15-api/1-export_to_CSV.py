#!/usr/bin/python3
"""export data into a csv file"""

import requests
import sys


if __name__ == "__main__":
    # url for the REST API
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]

    r = requests.get("{}/users/{}".format(url, userId))
    username = r.json().get('username')
    # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

    todos = requests.get("{}/todos?userId={}".format(url, userId))
    todos = todos.json()

    with open("{}.csv".format(userId), 'w') as file:
        for task in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(userId,
                               username, task.get('completed'),
                               task.get('title')))
