"""Process for downloading and saving a file
1. Call requests.get(link) -> Download the file.
2. Call open with 'wb' to create a new file in write binary code
3. Loop over the Response object's iter_content() method.
4. write() on each iteration to write the content to the file.
5. close() to close the file.
"""
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
	playFile.write(chunk)
playFile.close()
