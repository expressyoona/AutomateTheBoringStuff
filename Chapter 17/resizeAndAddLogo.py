#Resize all images in current working directory to in
#a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)

logoW, logoH = logoIm.size
logoIm = logoIm.resize((int(logoW/10),int(logoH/10)))
logoW, logoH = logoIm.size
os.makedirs('withLogo', exist_ok=True)
#TODO: Loop over all files in the working directory.
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
		continue
	im = Image.open(filename)
	w, h = im.size
	print(w, h)
	#TODO: Check if image needs to be resized.
	if w > SQUARE_FIT_SIZE and h > SQUARE_FIT_SIZE:
		#Calculate the new width and height to resize to.
		if w > h:
			h = int((SQUARE_FIT_SIZE / w) * h)
			w = SQUARE_FIT_SIZE
		else:
			w = int((SQUARE_FIT_SIZE / h) * w)
			h = SQUARE_FIT_SIZE
	print(w, h)
	#TODO: Resize the image.
	print('Resizing %s...' % filename)
	im = im.resize((w, h))
	#TODO: Add the logo.
	print('Adding logo to %s...' % filename)
	im.paste(logoIm, (w - logoW, h - logoH), logoIm)
	#TODO: Save changes.
	im.save(os.path.join('withLogo', filename))