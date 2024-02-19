#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
if __name__ == "__main__":
    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"
    # Fetch user data based on provided employee ID
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    # Fetch TODO list based on provided employee ID
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    # Extract completed tasks from the TODO list
    completed = [t.get("title") for t in todos if t.get("completed")]
    # Print employee's progress with tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
