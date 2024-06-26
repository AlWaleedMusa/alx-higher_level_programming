#!/usr/bin/python3
"""Get my GitHub user ID"""

import requests
import sys


def get_id(username, password):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data["id"]
        print(user_id)
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    get_id(username, password)
