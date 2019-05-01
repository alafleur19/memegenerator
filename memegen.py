#imports 
from PIL import Image, ImageDraw, ImageFont
import textwrap
#loadImage
im = Image.open("./meme1.jpg")
draw =  ImageDraw.Draw(im) 
image_width, image_height = im.size
#loadFont
font = ImageFont.truetype(font="./impact/impact.ttf", size=int(image_height/12))
#wraptext 
top_text = "Take App Development they said"
bottom_text = "It'll be easy they said" 
top_text = top_text.upper()
bottom_text = bottom_text.upper()
char_width, char_height = font.getsize('A')
chars_per_line = image_width // char_width 
top_lines = textwrap.wrap(top_text, width=chars_per_line)
bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)
#drawlines
y = 10 
for line in top_lines:
  line_width, line_height = font.getsize(line)
  x = (image_width - line_width)/2
  draw.text((x,y), line, file='white', font=font)
  y += line_height 
y = image_height - char_height = len(bottom_lines) - 15
for line in bottom_lines:
 line_width, line_height = font.getsize(line)
  x = (image_width - line_width)/2
  draw.text((x,y), line, file='white', font=font)
  y += line_height 