import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())
elems = exampleSoup.select('#author')
type(elems) #List
elems[0].getText() #'Al Sweigart'
str(elems[0]) #'<span id="author">Al Sweigart</span>'
elems[0].attrs #{'id': 'author'}
