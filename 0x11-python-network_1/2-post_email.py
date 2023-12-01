#!/usr/bin/python3
"""A script that:
- takes a URL,
- makes a POST request to it,
- takes the email as an argument,
- shows the body of the response
"""

import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line argument
    email = sys.argv[2]  # Get the email from command line argument

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')  # Encode the email as URL parameter

    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')  # Read and decode the body of the response

    print(body)
