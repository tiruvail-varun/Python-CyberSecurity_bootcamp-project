import os
import requests
from datetime import datetime
api_key = "88b3619296fbbbed15693f5e358b5874"
location = input("Enter city name : ")
complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print("**************************************************************")
print(f"Weather Stats for - {location} || {date_time}")
print("**************************************************************")
print("Current Temperature is: {:.2f} deg C".format(temp_city))
print("Current Weather dec:",weather_desc)
print("Current Humidity:",hmdt, "%")
print("Current Windspeed:",wind_spd,"kmph")
output = open('weather.txt','w')
output.write("**************************************************************\n")
output.write(f"Weather Stats for - {location} || {date_time}\n")
output.write("**************************************************************\n")
output.write("Current Temperature is: {:.2f} deg C".format(temp_city))
output.write(f"\nCurrent Weather dec: {weather_desc}\n")
output.write(f"Current Humidity: {hmdt}%\n")
output.write(f"Current Windspeed: {wind_spd} kmph\n")