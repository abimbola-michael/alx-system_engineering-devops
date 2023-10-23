#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/" + userId).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId), "w") as jsonFile:
        json.dump({
            userId: [{
                "task": togo.get("title"),
                "completed": todo.get("completed"),
                "username": username
                 } for todo in todos]
            }, jsonFile)
