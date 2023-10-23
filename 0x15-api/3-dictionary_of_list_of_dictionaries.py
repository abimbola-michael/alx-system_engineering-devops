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
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonFile:
        json.dump({
            user.get("id"): [{
                "task": togo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
                } for todo in requests.get(url + "todos", params={"userId": user.get("id")}).json()]
            for user in users}, jsonFile)
