#!/usr/bin/python3
"""A script that:
- takes your Github credentials,
- shows your id using Github API.
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, password))

if response.status_code == 200:
    data = response.json()
    user_id = data.get("id")
    print(user_id)
else:
    print("None")
