# requests_test.py
# read and get information from http

import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# raise an error if there is one
response.raise_for_status()

# create a variable to store the file
f = open("Romeo and Juliet.txt", "wb")

# grab info from http and save it in the variable
for chunk in response.iter_content(1000000):
    f.write(chunk)

# write the file to disk
f.close()