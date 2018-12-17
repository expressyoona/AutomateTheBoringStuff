import webbrowser, requests, bs4
def saveFile(url_link, filename):
	res = requests.get(url_link)
	playFile = open(filename, 'wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)
	playFile.close()
#Get
URL_link = 'https://google.com'
res = requests.get(URL_link)
res.raise_for_status()
#print(res.text)

soup = bs4.BeautifulSoup(res.text)
print(soup)
