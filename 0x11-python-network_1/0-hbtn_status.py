#!/usr/bin/python3
"""A script that fetches response from a certain URL using urllib package
"""

import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
