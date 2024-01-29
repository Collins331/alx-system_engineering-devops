#!/usr/bin/python3
"""import requests module"""
from sys import argv
import requests


if __name__ == "__main__":
    """
    prevents script execution when imported
    as a module in other programs
    """
    completed = 0
    total = 0
    title = []
    r = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    r = r.json()
    name = r.get("name")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
    t = requests.get(url)
    t = t.json()
    for i in t:
        if i.get("completed"):
            completed += 1
            total += 1
            title.append(i.get("title"))
        else:
            total += 1
    # print(t)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))
    for tc in title:
        print("\t {}".format(tc))
