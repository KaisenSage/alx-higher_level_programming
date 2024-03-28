# 0x11. Python - Network #1

This repository contains solutions to the tasks of the "0x11. Python - Network #1" project.

## Description

This project focuses on learning how to work with network-related tasks in Python. It covers fetching internet resources, making HTTP requests, handling responses, and interacting with APIs.

## Tasks

1. **0-hbtn_status.py**: A Python script that fetches https://alx-intranet.hbtn.io/status using the urllib package.
2. **1-hbtn_header.py**: A Python script that takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header.
3. **2-post_email.py**: A Python script that sends a POST request to a given URL with an email as a parameter.
4. **3-error_code.py**: A Python script that sends a request to a URL and displays the body of the response. Handles HTTP errors.
5. **4-hbtn_status.py**: A Python script that fetches https://alx-intranet.hbtn.io/status using the requests package.
6. **5-hbtn_header.py**: A Python script that takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using requests.
7. **6-post_email.py**: A Python script that sends a POST request to a given URL with an email as a parameter using requests.
8. **7-error_code.py**: A Python script that sends a request to a URL and displays the body of the response. Handles HTTP errors using requests.
9. **8-json_api.py**: A Python script that sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter and displays the response.
10. **10-my_github.py**: A Python script that uses the GitHub API to display the user's id.

## Requirements

- All scripts are written in Python 3.8.5
- Scripts are executed on Ubuntu 20.04 LTS
- pycodestyle is used for code formatting
- All modules have proper documentation
- Code should not execute when imported

## Usage

Each script can be executed from the command line. For example:

```bash
./0-hbtn_status.py
./1-hbtn_header.py https://example.com
./2-post_email.py http://example.com/submit_email myemail@example.com
# And so on...

