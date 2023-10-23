#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the CSV format
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    userId = sys.argv[1]
    user = requests.get(url + "users/" + userId).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csvFile:
        writer = csc.writer(csvFile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, username, todo.get("completed"), todo.get("title")]
            ) for todo in todos]
