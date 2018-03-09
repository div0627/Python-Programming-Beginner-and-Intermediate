''' This program Loop through each item in the weather_types list.
Check whether the item occurs in the new_weather list.
Append the result of the check to weather_type_found.
At the end, weather_type_found should be a list of Boolean values.
'''
weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for wea in weather_types:
    weather_type_found.append(wea in new_weather)
