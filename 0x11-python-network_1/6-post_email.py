#!/usr/bin/python3
"""A script that:
- takes a URL as an argument,
- makes a request to the URL,
- show the value of the X-Request-Id variable.
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]  # Get the URL from command line argument
    email = sys.argv[2]  # Get the email from command line argument

    payload = {'email': email}  # Create the payload with the email

    # Send a POST request with the payload
    response = requests.post(url, data=payload)

    print("Your email is: {}".format(email))
    print(response.text)  # Print the content of the response
