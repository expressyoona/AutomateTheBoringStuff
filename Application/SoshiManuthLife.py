import webbrowser
import requests
import bs4

def saveFile(url, filename):
	with open(filename, 'wb') as file:
		file.write(requests.get(url).content))
#Get
URK = 'https://soshi.manuth.life/data/soshi/pictures/ohgg/albums/lil-touch/'
res = requests.get(URL)
res.raise_for_status()
#print(res.text)

soup = bs4.BeautifulSoup(res.text)
print('----------------')
linkElems = soup.select('a')
for i in range(1, len(linkElems)):
	link_picture = URL + linkElems[i].get('href')
	saveFile(link_picture, 'Picture_' + str(i) + '.jpg')
print('Done!')
