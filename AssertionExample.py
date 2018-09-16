market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'green', 'ew': 'red'}
def switchLights(stoplight):
	for key in stoplight.keys():
		if stoplight[key] == 'green':
			stoplight[key] = 'yellow'
		if stoplight[key] == 'yellow':
			stoplight[key] = 'red'
		if stoplight[key] == 'red':
			stoplight[key] = 'green'
switchLights(market_2nd)