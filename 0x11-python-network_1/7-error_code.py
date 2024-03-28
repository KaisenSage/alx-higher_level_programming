#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the body of the response. If HTTP status code is >= 400, prints an error code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)

