#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
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
    # Write data to JSON file
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
