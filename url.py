#! /usr/bin/python
import requests
import argparse
import sys
import json


parser = argparse.ArgumentParser(description='Requests url and stores data as json or html')
parser.add_argument('url',help="enter url")
parser.add_argument('file', default='file.txt', help='Enter a file name')
parser.add_argument('--type',default='html',choices=['html','json'],help='Returns request in json file')
args = parser.parse_args()


result = requests.get("https://" + args.url)

if result.status_code >= 400:
    print(f"Error couldn not retrive {args.url}")

try:
    if args.type == 'html':
        content = result.text

    elif args.type == 'json' :
        content = json.dumps(result.json())

    with open(f'<file destination>args.file}','w', encoding='UTF-8') as file:
        file.write(content)

except ValueError:
        print("Error not json file")
