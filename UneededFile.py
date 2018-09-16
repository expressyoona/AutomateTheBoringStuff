import send2trash, os
conv = lambda x: x>>20
def findUneededFile(folder):
	folder = os.path.abspath(folder)
	Max = 0
	for foldernames, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			#print(foldernames + '\\' + filename)
			size = conv(os.path.getsize(os.path.join(foldernames, filename)))
			if size > 100:
				print(os.path.join(foldernames, filename) + ': ' + str(size) + 'MB')
			#print(filename + ' - ' + str(conv(size)) + ' KB')
			#print(filename)
findUneededFile('F:\\')
