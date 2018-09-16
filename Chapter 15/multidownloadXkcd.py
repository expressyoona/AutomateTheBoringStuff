#Downloads XKCD comics using multiple threads.
import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok = True)

def downloadXkcd(startComic, endComic):
	for urlNumber in range(startComic, endComic):
		#Download the page
		print('Downloading page https://xkcd.com/%s...' % urlNumber)
		res = requests.get('https://xkcd.com/%s' % urlNumber)
		#res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text)
		#Find the URL of the comic image.
		comicEle = soup.select('#comic img')
		if comicEle == []:
			print('Could not find comic image.')
		else:
			comicUrl = comicEle[0].get('src')
			#Download the image.
			print('\tDownloading image %s...' % comicUrl)
			res = requests.get('http:%s' % comicUrl)
			#res.raise_for_status()
			#Save the image to ./xkcd
			imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
			for chunk in res.iter_content(100000):
				imageFile.write(chunk)
			imageFile.close()
#TODO: Create and start the Thread object.
downloadThreads = []
for i in range(1, 200, 100):
	downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 98))
	downloadThreads.append(downloadThread)
	downloadThread.start()
#TODO: Wait for all threads to end.		
for downloadThread in downloadThreads:
	downloadThread.join()
print('Done!')