import requests
from pprint import pprint

#this program will show you the current information about weather in specific city in json

API_Key = 'a63ebfb740dbe99bbec8933295061f1e'

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?appid=" + API_Key + "&q=" + city
weather_data = requests.get(base_url).json()

pprint(weather_data)
