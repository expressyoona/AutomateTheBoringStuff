#Prints the weather for a location
import json, requests, sys
#Compute location from cmd.
if len(sys.argv) < 2:
	print('Usage: quickWeather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])
#TODO: Download the JSON data from OpenWeatherMap.org's API.
APPID = '41a9ead0bff81165aa88c8d116541d54'
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, APPID)
#print('Get data from:', url)
response = requests.get(url)
response.raise_for_status()
#TODO: Load JSON data into a Python varible
weatherData = json.loads(response.text)
#Print weather descriptions
print('Current weather in %s: ' % location)
w = weatherData['list']
print('\nToday:', w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('\nTomorrow:', w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('\nDay after tomorrow:', w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
#print('Done!')
