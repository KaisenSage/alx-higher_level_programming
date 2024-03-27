#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL with a specific header, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"

