#!/usr/bin/python
import argparse
import os
import requests
import sys

parser = argparse.ArgumentParser(description= 'Generates current weather data')
parser.add_argument('zip',type=str,help="enter zipcode for weather data")
parser.add_argument('--country', '-c',default='us',help="enter country abbreviation")

args = parser.parse_args()
api_key = os.getenv('OW_API')


if not api_key:
    print("API key does not exist for open weather")
    sys.exit(1)

url= f"https://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

result = requests.get(url)

if result.status_code !=200:
    print(f"Error retriving weather info {result.status_code}")
    sys.exit(1)

json_results = result.json()

temp = json_results['main']['temp']
sky = json_results['weather']

for item in sky:
    clouds = item['description']

conversion = (temp - 273.15) * (9 / 5) + 32

print(f"The temperature outside feels like {int(conversion)} Farenheit with {clouds}")
print(json_results)
