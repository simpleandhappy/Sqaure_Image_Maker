import sys
import os
from PIL import Image

if len(sys.argv) != 2:
    print("Usage: project.py filename")
    exit(1)
file_name = sys.argv[1]

if not os.path.exists(file_name):
    print("No file with name {file_name}")
    exit(1)

def make_square(file_name, min_size=256, fill_color=(0,0,0,0)):
    image = Image.open(file_name)
    x, y = image.size
    size = max(min_size, x, y)
    sq_image = Image.new('RGBA', (size, size), fill_color)
    sq_image.paste(image, (int((size - x) / 2), int((size - y) / 2)))
    return sq_image

sq_image = make_square("test.png")
sq_image.show()