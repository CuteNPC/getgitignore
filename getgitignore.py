#!/usr/bin/env python3

import requests
import sys

url = 'https://www.toptal.com/developers/gitignore/api/'

def main():

    if len(sys.argv) < 2:
        print('Usage: getgitignore <language>')
        sys.exit(1)

    language = sys.argv[1]
    response = requests.get(url + language)
    if response.status_code == 200:
        print(response.text)
        with open(".gitignore", 'a') as file:
            file.write(response.text + '\n')
    else:
        print('Error: Could not fetch .gitignore file for', language)

if __name__ == '__main__':
    main()

