from datetime import datetime

import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=13.754&longitude=100.5014&hourly=temperature_2m,relativehumidity_2m&timezone=Asia%2FBangkok'
result = requests.get(url)
values = result.json()

date_list = values['hourly']['time']
temp_list = values['hourly']['temperature_2m']
weather_dict = {}

for i in range(len(date_list)):
    weather_dict[date_list[i]] = temp_list[i]

max_date = max(weather_dict, key=weather_dict.get)
max_temp = weather_dict[max_date]

format_max_date = datetime.fromisoformat(max_date)
print('The hottest day in Bangkok is', max_temp, '°C at', format_max_date)
