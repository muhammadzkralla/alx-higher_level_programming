#!/usr/bin/python3
"""A script tha:
- takes a letter,
- makes aPOST request to http://0.0.0.0:5000/search_user.
"""
import requests
import sys

if len(sys.argv) > 1:
    letter = sys.argv[1]
else:
    letter = ""

url = "http://0.0.0.0:5000/search_user"
payload = {"q": letter}

response = requests.post(url, data=payload)

try:
    data = response.json()

    if data:
        print("[{}] {}".format(data["id"], data["name"]))
    else:
        print("No result")

except ValueError:
    print("Not a valid JSON")
