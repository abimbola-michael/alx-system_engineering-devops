#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/" + sys.argv[1]).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    comp_todos = [todo.get("title") for todo in todos if todo.get("completed")]
    print("Employee {} is done with tasks({}/{})".format(
        user.get("name"), len(comp_todos), len(todos)
        ))
    [print("\t {}".format(todo)) for todo in comp_todos]
