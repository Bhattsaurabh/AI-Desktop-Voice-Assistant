
from config import weatherapi
from say import say
import requests

def weatherReport(location):
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={weatherapi}")
    print(weather_data.json())
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    temp = round(temp - 274.15)
    say(f"the current temperature of {location} is {temp} degree celsius and weather is {weather}")

