#!/usr/bin/python3
"""A script that:
- takes a URL as an argument,
- receive response from a URL,
- show the value of the X-Request-Id variable
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        headers = response.headers
        x_request_id = headers.get('X-Request-Id')

    print(x_request_id)
