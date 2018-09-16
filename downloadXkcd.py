import requests, os, bs4
url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok = True)
while not url.endswith('#'):
	#TODO: Download the page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text)
	#TODO: Find the URL of the comic image.
	comicEle = soup.select('#comic img')
	if comicEle == []:
		print('Could not find comic image.')
	else:
		try:
			comicURL = 'https:' + comicEle[0].get('src')
			#TODO: Download the image.
			print('Downloading image %s...' % comicURL)
			res = requests.get(comicURL)
			res.raise_for_status()
		except requests.exceptions.MissingSchema:
			#Skip this comic
			prevLink = soup.select('a[rel="prev"]')[0]
			url = 'https://xkcd.com' + prevLink.get('href')
			continue
		#TODO: Save the image to ./xkcd
		imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
	#TODO: Get the Prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'https://xkcd.com' + prevLink.get('href')
print('Done!')
