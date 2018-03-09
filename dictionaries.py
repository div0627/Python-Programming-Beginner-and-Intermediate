''' This program Count how many times each type of weather occurs in the weather list, and store the results in a new dictionary called weather_counts.
When finished, weather_counts should contain a key for each different type of weather in the weather list, along with its associated frequency. Here's a preview of how the result should format the weather_counts dictionary (note that you'll be using real values, rather than the dummy ones below):
'''
weather_counts = {}
for item in weather:
    if item in weather_counts:
        weather_counts[item]+=1
    else:
        weather_counts[item]=1
