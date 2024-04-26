#!/usr/bin/python3
# script that takes in a letter and sends a POST request with a parameter

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    q = {"q": q}
    response = requests.post(url, data=q)

    try:
        response = response.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
