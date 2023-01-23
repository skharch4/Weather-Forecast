import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "8efb4754d6b02eafdac49a84e5bebbbc"
CITY = "Kyiv"

url= BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273
    return celsius
temp_kelvin = response['main']['temp']
temp_celsius=kelvin_to_celsius(temp_kelvin)
feels_like_kelvin = response ['main']['feels_like']
feels_like_celsius = kelvin_to_celsius (feels_like_kelvin)
description=response
sunrise_time= dt.datetime.utcfromtimestamp(response['sys'] ['sunrise'] + response['timezone'])
sunset_time= dt.datetime.utcfromtimestamp(response['sys'] ['sunset'] + response['timezone'])
humidity=response ['main']['humidity']
print(response)
print(f"Temperature in {CITY}: {temp_celsius: .2f}°C")
print(f"Temperature in {CITY} feels like: {feels_like_celsius: .2f}°C")
print(f"Sun rise in {CITY} in: {sunrise_time}")
print(f"Sun set in {CITY} in: {sunset_time}")
print(f"Humidity in {CITY} {humidity} %")










#open('api_key', 'r').read()

#list.sunset Sunset time, Unix, UTC
#list.temp
#list.temp.day Day temperature. Unit Default: Kelvin, Metric: Celsius, Imperial: Fahrenheit.
#print($temperature);
#json