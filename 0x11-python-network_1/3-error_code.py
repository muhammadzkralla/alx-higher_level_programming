#!/usr/bin/python3
"""A script that:
- takes a URL as an argument,
- sends a request to it,
- shows the body of the response.
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
