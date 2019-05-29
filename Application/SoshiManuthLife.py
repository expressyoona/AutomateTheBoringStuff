import webbrowser
import requests
import bs4

def saveFile(url, filename):
	with open(filename, 'wb') as file:
		file.write(requests.get(url).content))
#Get
URL_link = 'https://soshi.manuth.life/data/soshi/pictures/ohgg/albums/lil-touch/'
res = requests.get(URL_link)
res.raise_for_status()
#print(res.text)

soup = bs4.BeautifulSoup(res.text)
print('----------------')
linkElems = soup.select('a')
for i in range(1, len(linkElems)):
	link_picture = URL_link + linkElems[i].get('href')
	saveFile(link_picture, 'Picture_' + str(i) + '.jpg')
print('Done!')
