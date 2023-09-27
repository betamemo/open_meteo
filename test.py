# pip install requests (in your terminal)

from pprint import pprint

import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok'
result = requests.get(url)
pprint(result.json())

values = result.json()
print(values['hourly']['temperature_2m'])
