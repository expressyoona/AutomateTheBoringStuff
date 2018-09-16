#A folder called Photo folder if it has more than half of the files are photos.
#THe width and height of the picture must be larger than 500 px.
import os
from PIL import Image

for foldername, subfolders, filenames in os.walk('F:\\Photo'):
	numPhotoFiles = 0
	numNonPhotoFiles = 0
	for filename in filenames:
		#Check if file extension isnt png or jpg
		if not(filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.PNG')):
			numNonPhotoFiles += 1
			continue
		#Open image file using Pillow.
		#print(os.path.join(foldername, filename))
		try:
			im = Image.open(os.path.join(foldername, filename))
		except:
			print('Error when opening image %s' % os.path.join(foldername, filename))
		#Check if width & height are larger than 500.
		w, h = im.size
		if w > 500 and h > 500:
			#Image is large enough to be considered a photo.
			numPhotoFiles += 1
		else:
			#Image is too small to be a photo.
			numNonPhotoFiles += 1
	#print(numPhotoFiles, numNonPhotoFiles)
	#If more than half of files were photos,
	#print the absolute path of the folder.
	if numPhotoFiles > numNonPhotoFiles:
		print(os.path.abspath(foldername))
