"""This script asks the user for a city name and returns the weather information for that city for tomorrow.
The inforamtion is fetched using WeatherAPI.
Built as a part of GHW API using Copilot"""
import requests
import json
# Ask the user for a city name
city = input("Enter a city name: ")

# Make a request to the WeatherAPI
url = f"https://api.weatherapi.com/v1/forecast.json?key=ced049c5e5524dfb9f9105726240704&q={city}&days=2"
response = requests.get(url)

# print(response.text)  # Debugging

# Parse the JSON response
data = json.loads(response.text)

# Get the weather information for tomorrow
tomorrow = data['forecast']['forecastday'][1]
date = tomorrow['date']
condition = tomorrow['day']['condition']['text']
temp_c = tomorrow['day']['avgtemp_c']
temp_f = tomorrow['day']['avgtemp_f']

# Print the weather information for tomorrow
print(f"Tomorrow in {city}:")
print(f"Condition: {condition}")
print(f"Temperature: {temp_c}°C / {temp_f}°F")