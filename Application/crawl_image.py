import os
import sys
import requests
from bs4 import BeautifulSoup as BS


def save_image(image_url, filename):
    with open(filename, 'wb') as fi:
        fi.write(requests.get(image_url).content)


url = 'https://soshi.manuth.life/data/soshi/pictures/yoona/magazines/2019-may-harpers-bazaar-korea/'

res = requests.get(url)

if res.status_code is not 200:
    print('The URL does not exist!')
    sys.exit()

folder_name = url.split('/')[-2]
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
os.chdir(folder_name)
print(f'Switched to {folder_name} folder!')


soup = BS(res.text, 'lxml')
a_tag = soup.select('a')
total = len(a_tag)
for index, element in enumerate(a_tag):
    if index is 0:
        continue
    child_url = url + element.get('href')
    filename = child_url.split('/')[-1]
    print(f'Processing {child_url}')
    save_image(child_url, filename)
    print(f'[{index+1}/{total}] Saved {filename}')
