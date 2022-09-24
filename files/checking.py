import requests
import json
import sys

response = requests.get(url=f'http://ip-api.com/json/').json()

country = response.get('country')

if country.lower() == 'russia':
    sys.exit(1)