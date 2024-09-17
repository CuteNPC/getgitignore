#!/bin/bash

url='https://www.toptal.com/developers/gitignore/api/'

if [ "$#" -lt 1 ]; then
    echo 'Usage: getgitignore <language>'
    exit 1
fi

language="$1"
response=$(curl -sL "${url}${language}")

if [ $? -eq 0 ]; then
    echo "$response" >> .gitignore
    echo >> .gitignore
    echo ".gitignore file for $language fetched successfully"
else
    echo "Error: Could not fetch .gitignore file for $language"
fi
