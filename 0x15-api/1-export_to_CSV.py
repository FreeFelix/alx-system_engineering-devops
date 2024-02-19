#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys
if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    # Fetch user data based on provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    # Fetch TODO list based on provided employee ID
    todos = requests.get(url + "todos", params={"userId": user_id}).json()
    # Write data to CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
