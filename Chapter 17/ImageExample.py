#Handle image
from PIL import Image
cat = Image.open(filename)
w, h = cat.size
cat.filename
cat.format
cat.save(Another_filename)
cropped = cat.crop((335, 345, 565, 560))
"""

--- COPYING AND PASTING A PICTURE ONTO ANOTHER PICTURE ---
clone = picture.copy()
clone.paste(filename, top-left coordinate)

--- RESIZING A PICTURE ---
cat.resize((w, h)) -> Create a new picture

--- ROTATING A PICTURE ---
cat.rotate(degrees) -> Create a new picture

--- TRANSPOSING A PICTURE ---
cat.transpose(Image.FLIP_LEFT_RIGHT/FLIP_TOP_BOTTOM/TRANSPOSE/TRANSVERSE)


--- DRAWING SHAPES ---
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
	- Point
	- Line: draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
	- Rectangle: draw.rectangle((20, 30, 60, 60), fill='blue')
	- Ellipse: draw.ellipse((120, 30, 160, 60), fill='red')
	- Polygon: draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
   fill='brown')
im.save()

--- DRAWING TEXT ---
from PIL import ImageFont
draw.text((x, y), 'Your text', fill='Your color')
Your_font = ImageFont.truetype(path, size)
draw.text((x, y), 'Your text', fill='Your color', font = Your_font)
"""
Image.new('RGBA', (w, h)[, background_color])