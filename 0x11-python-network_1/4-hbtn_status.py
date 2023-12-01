#!/usr/bin/python3
"""fetches a specific url.
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)  # Send a GET request to the URL

    content = response.text  # Get the content of the response

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
