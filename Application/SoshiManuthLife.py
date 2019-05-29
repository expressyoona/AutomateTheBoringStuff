from bs4 import BeautifulSoup as BS
import requests
import sys
import os

def saveImage(url, filename):
	with open(filename, 'wb') as file:
		file.write(requests.get(url).content)

URL = 'https://soshi.manuth.life/data/soshi/pictures/yoona/other/160522-birthday-party/'

res = requests.get(URL)
if res.status_code != 200:
	print('URL does not exist!')
	sys.exit()

new_folder = URL.split('/')[-2].capitalize()

path = os.getcwd()

if not os.path.exists(new_folder):
	os.makedirs(new_folder)
	print('Created %s folder' % (new_folder))
	path = os.path.join(path, new_folder)
	os.chdir(path)
	print('Changed directory')
else:
	print('Folder already existed!')
	sys.exit()

soup = BS(res.text, features="lxml")
eles = soup.select('a')
total = len(eles) - 1
for i in range(1, len(eles)):
	child_url = URL + eles[i].get('href')
	file_name = child_url.split('/')[-1]
	saveImage(child_url, file_name)
	print('%d/%d. Stored %s' % (i, total, file_name))

print('Done!')