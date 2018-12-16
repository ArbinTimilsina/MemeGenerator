from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

first_line = input("First line?\n")
second_line_name = input("Second line name?\n")

img = Image.open("pic_in.png")
draw = ImageDraw.Draw(img)

# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("sans-serif.ttf", 40)

# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((20, 20),"{}".format(first_line), (0,0,0), font=font)
draw.text((20, 100),"{}: ".format(second_line_name), (0,0,0), font=font)
img.save('meme_out.png')
img.show()
