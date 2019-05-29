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
	"""
	res_other = requests.get(link_picture)
	soup_other = bs4.BeautifulSoup(res_other.text)
	playFile = open('Picture_' + str(i) + '.jpg', 'wb')
	for chunk in res.iter_content(100000):
		playFile.write(chunk)
		"""
#playFile.close()
print('Done!')
